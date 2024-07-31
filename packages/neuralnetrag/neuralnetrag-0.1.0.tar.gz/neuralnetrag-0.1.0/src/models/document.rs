#[derive(Debug, Clone)]
pub struct Document {
    pub content: String,
}

impl Document {
    pub fn new(content: &str) -> Self {
        Self {
            content: content.to_string(),
        }
    }

    pub fn tokenize(&self) -> Vec<&str> {
        self.content.split_whitespace().collect()
    }
}
