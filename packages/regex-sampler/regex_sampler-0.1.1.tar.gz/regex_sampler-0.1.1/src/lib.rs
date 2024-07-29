use pyo3::prelude::*;

mod decoders;
use decoders::{iter_decoder::IterDecoder, token::Token, trie_decoder::TrieDecoder};

#[pymodule]
fn regex_sampler(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<TrieDecoder>()?;
    m.add_class::<IterDecoder>()?;
    m.add_class::<Token>()?;
    Ok(())
}
