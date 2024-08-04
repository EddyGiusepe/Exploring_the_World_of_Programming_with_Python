#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Este script resume um PDF em vários parágrafos e motiva a seguir
a rede social do escritor
"""
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain.tools import tool
import requests
from PyPDF2 import PdfReader
import re

# 1. Definindo variávei de Ambiente: 
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

# 2. Escolho o modelo para os agentes:
model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.2) # "gpt-4o"   ou  "gpt-4o-mini"  ou  "gpt-3.5-turbo-0125"

# 3. Tool para buscar e pré-processar conteúdo PDF:
@tool
def fetch_pdf_content(url: str) -> str:
    """
    Busca e pré-processa conteúdo de um PDF dado seu URL.
    Retorna o texto do PDF.
    """
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    with open('temp.pdf', 'rb') as f:
        pdf = PdfReader(f)
        text = '\n'.join(page.extract_text() for page in pdf.pages if page.extract_text())

    # Pré-processamento opcional de texto:
    processed_text = re.sub(r'\s+', ' ', text).strip()
    return processed_text

# 4. Agentes:
# 4.1 Agente de leitura de PDF:
pdf_reader = Agent(
    role='Extrator de conteúdo PDF',
    goal='Extrair e pré-processar texto de um PDF',
    backstory='Especializado em manipulação e interpretação de documentos PDF',
    verbose=True,
    tools=[fetch_pdf_content],
    allow_delegation=False,
    llm=model
)

# 4.2 Agente Escritor de Artigos:
article_writer = Agent(
    role='Criador do artigo',
    goal='Escreva um artigo conciso e interessante',
    backstory='Especialista em criar artigos informativos e interessantes',
    verbose=True,
    allow_delegation=False,
    llm=model
)

# 4.3 Agente criador do título:
title_creator = Agent(
    role='Gerador de Títulos',
    goal='Gere um título atraente para o artigo',
    backstory='Hábil na criação de títulos envolventes e relevantes',
    verbose=True,
    allow_delegation=False,
    llm=model
)

# 4.4 Agente Integrador CTA:
cta_integrator = Agent(
    role='Integrador de Chamada para Ação',
    goal='Incorpore uma chamada para ação para seguir uma conta do Facebook',
    backstory='Especializado em criar chamadas para ação eficazes',
    verbose=True,
    allow_delegation=False,
    llm=model
)

# 5. Tarefas:
# 5.1 Tarefa que lê e processa PDF:
def pdf_reading_task(pdf_url):
    return Task(
        description=f"Leia e pré-processe o texto do PDF desta URL: {pdf_url}",
        agent=pdf_reader,
        expected_output="O texto processado ou extraído do PDF."
    )
# 5.2 Tarefa que escreve o artigo:
task_article_drafting = Task(
    description="Crie um artigo conciso com 4 ou 6 parágrafos com base no conteúdo extraído do PDF.",
    agent=article_writer,
    expected_output="Um resumo de 4 ou 6 parágrafos."
)
# 5.3 Tarefa que cria o Título:
task_title_generation = Task(
    description="Crie um título envolvente e relevante para o artigo.",
    agent=title_creator,
    expected_output="O título deve ser interessante e que faça sentido com a escrita do artigo."
)
# 5.4 Tarefa que incentiva a seguir no Twitter:
def task_cta_addition(twitter_url):
    return Task(
        description=f"Incluir uma chamada para ação no final do artigo, incentivando os leitores a seguir esta conta do Facebook: {twitter_url}",
        agent=cta_integrator,
        expected_output="Motivando a seguir a conta do Facebook "
    )

# 6. Entradas do Usuário:
pdf_url = input("Insira o URL do PDF: ")
twitter_url = input("Insira sua URL do Facebook: ")

# 7. Instanciar e executar crew:
crew = Crew(
    agents=[pdf_reader, article_writer, title_creator, cta_integrator],
    tasks=[pdf_reading_task(pdf_url), task_article_drafting, task_title_generation, task_cta_addition(twitter_url)],
    verbose=2
)

# 8. Execute o crew:
result = crew.kickoff()
print(f"🤗🤗🤗{result}🤗🤗🤗")
# 9. Combinar resultados:
#final_article = f"{task_title_generation.output.result}\n\n{task_article_drafting.output.result}\n\nSiga me no Facebook: {twitter_url}"
print("--------------------------")
#print(final_article)
