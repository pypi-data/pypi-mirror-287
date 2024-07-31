use reqwest;
use scraper::{Html, Selector};
use std::error::Error;
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

fn extract_text_from_url(url: &str) -> Result<String, Box<dyn Error>> {
    let body = reqwest::blocking::get(url)?.text()?;
    let document = Html::parse_document(&body);
    let selector = Selector::parse("p").unwrap();

    let mut content = String::new();
    for element in document.select(&selector) {
        content.push_str(&element.text().collect::<Vec<_>>().join(" "));
        content.push(' ');
    }
    Ok(content)
}

fn extract_texts_from_urls(urls: &[&str]) -> Result<Vec<String>, Box<dyn Error>> {
    let mut documents = Vec::new();
    for &url in urls {
        match extract_text_from_url(url) {
            Ok(content) => documents.push(content),
            Err(e) => eprintln!("Failed to fetch data from {}: {}", url, e),
        }
    }
    Ok(documents)
}

#[pyfunction]
fn extract_texts(urls: Vec<&str>) -> PyResult<Vec<String>> {
    match extract_texts_from_urls(&urls) {
        Ok(docs) => Ok(docs),
        Err(e) => Err(PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e.to_string())),
    }
}

// Placeholder for actual response generation function
#[pyfunction]
fn generate_response(query: String, documents: Vec<String>) -> PyResult<String> {
    Ok(format!("Response for query '{}' with {} documents", query, documents.len()))
}

#[pymodule]
fn neuralnetrag(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(extract_texts, m)?)?;
    m.add_function(wrap_pyfunction!(generate_response, m)?)?;
    Ok(())
}
