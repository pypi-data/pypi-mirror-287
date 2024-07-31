pub struct Generator;

impl Generator {
    pub fn new() -> Self {
        Self
    }

    pub fn generate(&self, document: &str, query: &str) -> String {
        format!("Based on the document: '{}' and your query: '{}', the system recommends...", document, query)
    }
}
