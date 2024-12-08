#!/usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Ollama-OCR
==========
Um poderoso pacote OCR (Optical Character Recognition) que permite extrair texto de imagens.
Este pacote usa modelos de Linguagem de Visão de última geração por meio do Ollama.

Link de estudo ---> https://github.com/imanoop7/Ollama-OCR/tree/main

Instalação ---> pip install ollama-ocr
"""
from ollama_ocr import OCRProcessor

# Inicializamos o processador de OCR:
ocr = OCRProcessor(model_name='llama3.2-vision:11b', # Você pode usar qualquer modelo de visão disponível no Ollama
                   max_workers=10)
# Processamos uma imagem:
result = ocr.process_image(
    image_path="/home/eddygiusepe/2_EddyGiusepe_Estudo/Exploring_the_World_of_Programming_with_Python/41_Multimodal_Embeddings_Ollama-Vision/images/placa_Motor_ROTADA.jpg",
    format_type="text",  # Opções: markdown, text, json, structured, key_value
    preprocess=True
)

print(result)
