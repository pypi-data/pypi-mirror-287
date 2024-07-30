use super::token::Token;

use std::{collections::VecDeque, usize};
use regex_automata::{hybrid::{dfa::{Cache, DFA}, LazyStateID}, util::start, Anchored};
use rustc_hash::{FxHashMap, FxHashSet};
use pyo3::prelude::*;

#[pyclass]
pub struct TrieDecoder {
    dfa: DFA,
    trie: Trie,
    stop_token_ids: Vec<usize>
}
impl TrieDecoder{
    fn is_final(&mut self, cache: &Cache, state: LazyStateID) -> bool {
        return self.dfa.next_eoi_state(&mut cache.clone(), state).unwrap().is_match()
    }
    fn decode(&mut self, cache: &mut Cache, text: &str, start: LazyStateID) -> LazyStateID {
        let mut state: LazyStateID = start;
        for &char in text.as_bytes().iter() {
            state = self.dfa.next_state(cache, state, char).unwrap();
        }
        return state;
    }
}
#[pymethods]
impl TrieDecoder{
    #[new]
    fn new(pattern: &str, tokens: Vec<Token>, stop_token_ids: Vec<usize>) -> TrieDecoder {
        let dfa = DFA::new(pattern).expect("Failed to compile regex");
        let mut trie = Trie::new();
        let stops = FxHashSet::from_iter(stop_token_ids.iter().cloned());
        for token in tokens {
            if !stops.contains(&token.id) {
                trie.insert(&token.text, token.id);
            }
        }
        TrieDecoder { dfa, trie, stop_token_ids}
    }

    fn get_valid_token_ids(&mut self, prefix_str: &str) -> Vec<usize> {
        let config = start::Config::new().anchored(Anchored::Yes);
        let mut cache = self.dfa.create_cache();
        let mut prefix_state = self.dfa.start_state(&mut cache, &config).expect("Failed to get start state");
        prefix_state = self.decode(&mut cache, prefix_str, prefix_state);
        let prefix_final = self.is_final(&cache, prefix_state);
        let mut output: Vec<usize> = Vec::new();
        if prefix_final {
            for &stop_token in &self.stop_token_ids {
                output.push(stop_token);
            }
        }
        let mut queue: VecDeque<(usize, LazyStateID, Cache)> = VecDeque::new();
        queue.push_front((0, prefix_state, cache.clone()));
        while !queue.is_empty() {
            let (index, state, cache) = queue.pop_front().unwrap();
            if let Some(tok_id) = self.trie.is_final.get(&index) {
                if state.is_match() && match self.dfa.next_eoi_state(&mut cache.clone(), state){
                    Ok(f_state) => f_state.is_match(),
                    Err(_) => false
                } || !state.is_tagged() {
                    output.push(*tok_id);
                }
            }
            for (&byte, &next_state) in &self.trie.nodes[index] {
                let mut token_cache = cache.clone();
                if let Ok(trans_state) = self.dfa.next_state(&mut token_cache, state, byte) {
                    if !trans_state.is_dead() && !trans_state.is_quit() {
                        queue.push_front((next_state, trans_state, token_cache));
                    }
                }
            }
        }
        output
    }
}


struct Trie {
    pub nodes: Vec<FxHashMap<u8, usize>>, // node_id -> {byte -> node_id}
    pub is_final: FxHashMap<usize, usize> // node_id -> tok_id
}

impl Trie {
    fn new() -> Trie {
        Trie {
            nodes: vec![FxHashMap::default()],
            is_final: FxHashMap::default() 
        }
    }

    fn insert(&mut self, word: &str, id: usize) {
        let mut current_node: usize = 0;
        for &byte in word.as_bytes().iter() {
            let next_node = match self.nodes[current_node].get(&byte) {
                Some(&node) => node,
                None => {
                    let new_node = self.nodes.len();
                    self.nodes.push(FxHashMap::default());
                    self.nodes[current_node].insert(byte, new_node);
                    new_node
                }
            };
            current_node = next_node;
        }
        if let Some(_) = self.is_final.insert(current_node, id){
            panic!("Duplicate tokens found during trie construction: {}, {}", word, id);
        }
    }
}