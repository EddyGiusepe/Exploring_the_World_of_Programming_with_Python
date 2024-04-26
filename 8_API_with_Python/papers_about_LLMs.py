#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

paperswithcode.com ---> https://paperswithcode.com/
"""
import urllib.parse
import requests
import json
from tqdm import tqdm

def extract_papers(query: str, num_pages: int = None, save_to_file: str = None):
    query = urllib.parse.quote(query)
    url = f"https://paperswithcode.com/api/v1/papers/?q={query}"
    response = requests.get(url)
    response = response.json()
    count = response["count"]
    results = response["results"]

    # Determinar o número de páginas a serem buscadas
    if num_pages is None:
        num_pages = (count + 49) // 50  # Arredonda para cima a divisão de count por 50

    # Iterar sobre as páginas de resultados
    for page in tqdm(range(2, num_pages + 1)):
        page_url = f"https://paperswithcode.com/api/v1/papers/?page={page}&q={query}"
        page_response = requests.get(page_url)
        page_response = page_response.json()

        # Verificar se a chave 'results' está presente no dicionário de resposta
        if "results" in page_response:
            results += page_response["results"]
        else:
            print(f"A chave 'results' não está presente no dicionário de resposta para a página {page}.")

    # Salvar os papers em um arquivo JSON se save_to_file for fornecido
    if save_to_file:
        with open(save_to_file, 'w') as f:
            json.dump(results, f)

    return results

# Exemplo de uso:
query = "PYANNOTE.AUDIO"
papers = extract_papers(query, num_pages=5, save_to_file="papers.json")
print(len(papers))
