use std::collections::HashMap;
use crate::tokenizer::tokenize;

pub struct Retriever {
    documents: Vec<String>,
}

impl Retriever {
    pub fn new(documents: Vec<String>) -> Self {
        Self { documents }
    }

    fn count_words(tokens: &[&str]) -> HashMap<&str, usize> {
        let mut counter = HashMap::new();
        for &token in tokens {
            *counter.entry(token).or_insert(0) += 1;
        }
        counter
    }

    fn cosine_similarity(query: &str, document: &str) -> f64 {
        let query_tokens = tokenize(query);
        let document_tokens = tokenize(document);
        let query_counter = Self::count_words(&query_tokens);
        let document_counter = Self::count_words(&document_tokens);

        let dot_product = query_counter.iter().fold(0, |acc, (key, val)| {
            acc + val * document_counter.get(key).unwrap_or(&0)
        });

        let magnitude_query = (query_counter.values().fold(0, |acc, &val| acc + (val * val) as f64)).sqrt();
        let magnitude_document = (document_counter.values().fold(0, |acc, &val| acc + (val * val) as f64)).sqrt();

        if magnitude_query > 0.0 && magnitude_document > 0.0 {
            (dot_product as f64) / (magnitude_query * magnitude_document)
        } else {
            0.0
        }
    }

    pub fn retrieve(&self, query: &str) -> String {
        let best_match = self.documents.iter()
            .max_by(|&doc1, &doc2| {
                Self::cosine_similarity(query, doc1)
                    .partial_cmp(&Self::cosine_similarity(query, doc2))
                    .unwrap_or(std::cmp::Ordering::Equal)
            })
            .unwrap_or(&String::from("No relevant document found"));

        best_match.clone()
    }
}
