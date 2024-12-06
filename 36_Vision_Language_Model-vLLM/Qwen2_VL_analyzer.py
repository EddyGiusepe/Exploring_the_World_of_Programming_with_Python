#!/usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Qwen2-VL
========
Aqui usamos o modelo Qwen2-VL para análise de imagens.
"""
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Union, Tuple, Optional
import torch
from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from qwen_vl_utils import process_vision_info

# Constantes:
AVAILABLE_MODELS = {
    "2B": "Qwen/Qwen2-VL-2B-Instruct",
    "7B": "Qwen/Qwen2-VL-7B-Instruct",
    "72B": "Qwen/Qwen2-VL-72B-Instruct"
}

SYSTEM_PROMPT = """Você é um experto em Análise de Vibração, Manutenção preditiva
                   e monitoramento de ativos industriais."""

@dataclass
class ImageInput:
    """Classe para armazenar informações da imagem de entrada."""
    file_path: Path
    resized_height: int = 696
    resized_width: int = 943


class Qwen2VLAnalyzer:
    """
    Classe principal para análise de imagens usando o modelo Qwen2-VL.
    
    Attributes:
        model_size (str): Tamanho do modelo ('2B', '7B' ou '72B')
        device (str): Dispositivo para processamento ('cuda' ou 'cpu')
        model: Modelo Qwen2-VL carregado
        processor: Processador para o modelo
    """
    
    def __init__(self, model_size: str = "2B", device: str = "cuda") -> None:
        if model_size not in AVAILABLE_MODELS:
            raise ValueError(f"Modelo inválido. Escolha entre: {list(AVAILABLE_MODELS.keys())}")
            
        self.model_size = model_size
        self.device = device
        self.model = self._load_model()
        self.processor = self._load_processor()
    
    def _load_model(self) -> Qwen2VLForConditionalGeneration:
        """Carrega o modelo Qwen2-VL."""
        return Qwen2VLForConditionalGeneration.from_pretrained(
            AVAILABLE_MODELS[self.model_size],
            torch_dtype="auto",
            device_map=self.device
        )
    
    def _load_processor(self) -> AutoProcessor:
        """Carrega o processador para o modelo."""
        return AutoProcessor.from_pretrained(AVAILABLE_MODELS[self.model_size])
    
    def _prepare_messages(self, image_input: ImageInput, query: str) -> List[Dict]:
        """Prepara a mensagem para o modelo."""
        return [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "image": str(image_input.file_path),
                        "resized_height": image_input.resized_height,
                        "resized_width": image_input.resized_width,
                    },
                    {
                        "type": "text",
                        "text": query
                    }
                ]
            }
        ]
    
    def analyze_image(self, image_input: ImageInput, query: str) -> str:
        """
        Analisa uma imagem e retorna a resposta do modelo.
        
        Args:
            image_input (ImageInput): Dados da imagem a ser analisada
            query (str): Pergunta ou instrução para o modelo
            
        Returns:
            str: Resposta do modelo
        """
        messages = self._prepare_messages(image_input, query)
        text = self.processor.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        
        image_inputs, video_inputs = process_vision_info(messages)
        inputs = self.processor(
            text=[text],
            images=image_inputs,
            videos=video_inputs,
            padding=True,
            return_tensors="pt",
        ).to(self.device)
        
        generated_ids = self.model.generate(**inputs, max_new_tokens=512)
        generated_ids_trimmed = [
            out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
        ]
        
        output_text = self.processor.batch_decode(
            generated_ids_trimmed, 
            skip_special_tokens=True, 
            clean_up_tokenization_spaces=True
        )
        
        return output_text[0]
    