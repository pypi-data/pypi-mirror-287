from typing import List, Callable, Union
from transformers import PreTrainedTokenizerBase, LlamaTokenizerFast, LlamaTokenizer
import torch
from collections import Counter
from .regex_sampler import Token, TrieDecoder


def get_llama_tokens(tokenizer: Union[LlamaTokenizer, LlamaTokenizerFast], token: str) -> str:
    str_token = tokenizer.convert_tokens_to_string([token])
    if token.startswith(chr(9601)):
        return " " + str_token
    elif token == "<0x20>":
        return " "
    return str_token

def is_llama_tokenizer(tokenizer: PreTrainedTokenizerBase) -> bool:
    return isinstance(tokenizer, LlamaTokenizer) or isinstance(tokenizer, LlamaTokenizerFast)

def get_string_token(tokenizer: PreTrainedTokenizerBase, token: str) -> str:
    if is_llama_tokenizer(tokenizer):
        return get_llama_tokens(tokenizer, token)
    return tokenizer.convert_tokens_to_string([token])
    

def prefix_token_fn_generator(tokenizer: PreTrainedTokenizerBase, pattern: str) -> Callable[[int, torch.Tensor], List[int]]:
    tokens = []
    seen = {}
    for token, token_id in sorted(tokenizer.get_vocab().items(), key=lambda x: x[1]):
        string_token = get_string_token(tokenizer, token)
        if string_token in seen:
            continue
        seen[string_token] = token_id
        tokens.append(Token(string_token, token_id))
    trie_decoder = TrieDecoder(pattern, tokens, [tokenizer.eos_token_id])
    gen_start_token_id = None
    prompt_text = ""
    def prefix_token_fn(batch_id: int, input_ids: torch.Tensor) -> List[int]:
        nonlocal gen_start_token_id
        nonlocal prompt_text
        if gen_start_token_id is None:
            gen_start_token_id = len(input_ids)
            prompt_text = tokenizer.decode(input_ids)
        decoded = tokenizer.decode(input_ids)[len(prompt_text):] # bruh
        return trie_decoder.get_valid_token_ids(decoded)
    return prefix_token_fn