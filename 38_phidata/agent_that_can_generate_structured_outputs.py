#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

=========================================
Agente que pode gerar saídas estruturadas
=========================================
Um dos nossos recursos favoritos do LLM é gerar dados
estruturados (ou seja, um modelo pydantic) a partir do
texto. Use esse recurso para extrair recursos, gerar scripts 
de filmes, produzir dados falsos etc.

Github: https://github.com/phidatahq/phidata?tab=readme-ov-file#agent-that-can-generate-structured-outputs
"""
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
#openai.api_key  = os.environ['OPENAI_API_KEY']
#Eddy_key_openai  = os.environ['OPENAI_API_KEY']
#from openai import OpenAI
#client = OpenAI(api_key=Eddy_key_openai)


# Vamos criar um agente de filmes para escrever um MovieScriptpara nós:
from typing import List
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from pydantic import BaseModel, Field

class MovieScript(BaseModel):
    setting: str = Field(..., description="Crie um cenário agradável para um filme de sucesso.")
    ending: str = Field(..., description="Final do filme. Se não estiver disponível, forneça um final feliz.")
    genre: str = Field(..., description="Gênero do filme. Se não estiver disponível, selecione ação, suspense ou comédia romântica.")
    name: str = Field(..., description="Dê um nome a este filme")
    characters: List[str] = Field(..., description="Nome dos personagens deste filme.")
    storyline: str = Field(..., description="História de 3 frases para o filme. Faça-o emocionante!")

# Agent that uses JSON mode:
json_mode_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="Você escreve roteiros de filmes.",
    response_model=MovieScript,
    structured_outputs=False,
)

# Agent that uses structured outputs:
structured_output_agent = Agent(
    model=OpenAIChat(id="gpt-4o-2024-08-06"),
    description="Você escreve roteiros de filmes.",
    response_model=MovieScript,
    structured_outputs=True,
)

json_mode_agent.print_response("Perú")
print("")
structured_output_agent.print_response("Perú", show_message=False, markdown=True, stream=True)
