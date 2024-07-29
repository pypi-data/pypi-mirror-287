use pyo3::prelude::*;


#[derive(Clone, Debug)]
#[pyclass]
pub struct Token {
    pub text: String,
    pub id: usize
}
#[pymethods]
impl Token {
    #[new]
    pub fn new(text: &str, id: usize) -> Token {
        Token {text: text.to_string(), id}
    }
}