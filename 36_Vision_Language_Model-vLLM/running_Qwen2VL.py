#!/usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Executando o modelo Qwen2-VL
============================
Este script executa o modelo Qwen2-VL para análise de imagens.
"""
from pathlib import Path
from Qwen2_VL_analyzer import Qwen2VLAnalyzer, ImageInput

# Inicializar o analisador:
analyzer = Qwen2VLAnalyzer(model_size="2B", device="cuda")

# Preparar entrada da imagem
image_input = ImageInput(
    file_path=Path("/home/eddygiusepe/2_EddyGiusepe_Estudo/Exploring_the_World_of_Programming_with_Python/41_Multimodal_Embeddings_images-audio-video/images/placa_motor_monofasico.JPG")
)

# Fazer a análise:
query = "Extraia, APENAS, o tipo de motor."
resultado = analyzer.analyze_image(image_input, query)
print(resultado)
