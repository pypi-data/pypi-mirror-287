pub fn tokenize(text: &str) -> Vec<&str> {
    text.split_whitespace().collect()
}
