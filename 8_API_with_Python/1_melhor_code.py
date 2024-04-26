#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

paperswithcode.com ---> https://paperswithcode.com/

Baixando Dados do paperswithcode
================================
Aqui apenas baixamo os dados do link acima.
Aqui usamos um classe para trabalhar com os 
parâmetros e para deixar o código mais simples,
mais legível.
"""

import gdown
import json
import urllib.parse
import requests
from pydantic import BaseModel


class RawLocation(BaseModel):
    url: str
    path_to_save: str

def generate_query_url(query: str, base_url: str) -> str:
    query = urllib.parse.quote(query)
    return f"{base_url}?q={query}"


def download_data(raw_location: RawLocation) -> None:
    response = requests.get(raw_location.url)
    if response.status_code == 200:
        with open(raw_location.path_to_save, 'w') as f:
            json.dump(response.json(), f)
    else:
        print(f"Falha ao recuperar dados. Código de status: {response.status_code}")


if __name__=="__main__":
    base_url = "https://paperswithcode.com/api/v1/papers/"
    query = "Large Language Models"
    # Primeiro escrevo minha query:
    query_url = generate_query_url(query, base_url)
    # Seguidamente, baixamos os dados:
    raw_location = RawLocation(url=query_url, path_to_save="papers.json")
    download_data(raw_location)
