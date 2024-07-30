use std::collections::HashSet;
use super::token::Token;
use regex_automata::{hybrid::{dfa::{Cache, DFA}, LazyStateID}, util::start, Anchored};
use pyo3::prelude::*;

#[pyclass]
pub struct IterDecoder {
    dfa: DFA,
    tokens: Vec<Token>,
    stop_token_ids: HashSet<usize>

}
impl IterDecoder{
    fn is_final(&mut self, cache: &mut Cache, state: LazyStateID) -> bool {
        return self.dfa.next_eoi_state(cache, state).unwrap().is_match()
    }

    fn decode(&self, cache: &mut Cache, text: &str, start_state: LazyStateID) -> LazyStateID {
        let mut state = start_state;
        for &char in text.as_bytes().iter() {
            state = self.dfa.next_state(cache, state, char).expect("Expected valid cache");
        }
        return state;
    }
}
#[pymethods]
impl IterDecoder {
    #[new]
    fn new(pattern: &str, tokens: Vec<Token>, stop_token_ids: Vec<usize>) -> IterDecoder {
        let dfa = DFA::new(pattern).expect("Failed to compile regex");
        IterDecoder { dfa, tokens, stop_token_ids: HashSet::from_iter(stop_token_ids.into_iter())}
    }

    fn get_valid_token_ids(&mut self, prefix_str: &str) -> Vec<usize> {
        let config = start::Config::new().anchored(Anchored::Yes);
        let mut cache = self.dfa.create_cache();
        let mut prefix_state = self.dfa.start_state(&mut cache, &config).expect("Failed to get start state");
        prefix_state = self.decode(&mut cache, prefix_str, prefix_state);
        let prefix_final = self.is_final(&mut cache.clone(), prefix_state);
        if prefix_state.is_dead() {
            panic!("Starting text cannot lead to matching regex!");
        }
        let mut output: Vec<usize> = Vec::new();
        let tokens = self.tokens.clone();
        for token in tokens {
            let token_cache = &mut cache.clone(); // Must clone for each token due to cache states only being valid for fixed generation pattern.
            let res = self.decode(token_cache, &token.text, prefix_state);
            if prefix_final && self.stop_token_ids.contains(&token.id){
                output.push(token.id);
                continue;
            }

            if res.is_match() {
                let f_state = self.dfa.next_eoi_state(token_cache, res).expect("Expected valid cache");
                if f_state.is_match() {
                    output.push(token.id);
                }
            } else if !res.is_dead(){
                output.push(token.id);
            }
        }
        
        output
    }
}
