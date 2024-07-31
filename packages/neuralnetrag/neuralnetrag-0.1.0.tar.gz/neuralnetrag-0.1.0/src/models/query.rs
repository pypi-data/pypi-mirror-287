#[derive(Debug, Clone)]
pub struct Query {
    pub original: String,
    pub tokens: Vec<String>,
}

impl Query {
    pub fn new(original: &str) -> Self {
        let tokens = original.split_whitespace().map(|s| s.to_string()).collect();
        Self {
            original: original.to_string(),
            tokens,
        }
    }

    pub fn tokenize(&self) -> Vec<&str> {
        self.tokens.iter().map(AsRef::as_ref).collect()
    }
}
