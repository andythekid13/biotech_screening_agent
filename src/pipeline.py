import requests
import os

def query_pubmed(query):
    api_key = os.getenv('NCBI_API_KEY')
    if not api_key:
        raise ValueError("NCBI API key not found. Set it in the .env file.")
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        'db': 'pubmed',
        'term': query,
        'retmode': 'json',
        'api_key': api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data from PubMed: {response.text}")
    return response.json()

def extract_biotech_steps(text):
    # Placeholder for processing biotech steps using an NLP model
    return f"Extracted steps for: {text}"
