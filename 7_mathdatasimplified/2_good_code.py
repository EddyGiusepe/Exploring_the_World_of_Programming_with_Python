#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Lendo cada arquivo de .xml
==========================
Neste script a função construída aqui apenas vai 
extrair o conteúdo de um arquivo .xml. Para isso você
deve passar o PATH de dito arquivo .xml.
"""
import xml.etree.ElementTree as ET


def extract_texts_from_each_file(file_path: str) -> str:
    list_of_text_in_one_file = [r.text for r in ET.parse(file_path).getroot()[0]]
    return " ".join(list_of_text_in_one_file)





if __name__ == "__main__":
    file_path = "/home/eddygiusepe/1_Eddy_Giusepe/Exploring_the_World_of_Programming_with_Python/7_mathdatasimplified/Data/train/en/1a4a60942a15426c9a7ec3764e7d0ede.xml"
    texts_each = extract_texts_from_each_file(file_path=file_path)
    print(texts_each)