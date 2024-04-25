#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Extraindo o Text de todos os arquivos .xml
===========================================
Este script extrai todos os textos de todos os arquivos
.xml (os .xml estão dentro de uma pasta). Para isso se
adicionou mais uma função e se adicionou um LOOP que 
percorre todos os arquivos .xml.
"""
import xml.etree.ElementTree as ET
from pathlib import Path


def extract_texts_from_multiple_files(folder_path: str) -> str:
    all_docs = []
    for file_path in Path(folder_path).glob("*.xml"):
        text_in_one_file = extract_texts_from_each_file(file_path)
        all_docs.append(text_in_one_file)

    return " ".join(all_docs)


def extract_texts_from_each_file(file_path: str) -> str:
    list_of_text_in_one_file = [r.text for r in ET.parse(file_path).getroot()[0]]
    return " ".join(list_of_text_in_one_file)




if __name__ == "__main__":
    folder_path = "./Data/train/en"
    texts_all =  extract_texts_from_multiple_files(folder_path=folder_path)
    print(texts_all)