#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

crewAI
======
Aqui realizo um exemplo, de uso Básico, do Framework 🤖 crewAI de ponta
para orquestrar agentes de IA autônomos e role-playing. Ao promover a inteligência
colaborativa, a 🤖 CrewAI capacita os agentes a trabalharem juntos de forma integrada,
lidando com tarefas complexas.

Install
=======
$ pip install crewai
$ pip install 'crewai[tools]'
"""
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI

import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
#openai.api_key  = os.environ['OPENAI_API_KEY']
#Eddy_key_openai  = os.environ['OPENAI_API_KEY']

#from openai import OpenAI
#client = OpenAI(api_key=Eddy_key_openai)


# 1. Definimos nossos dois Agentes:
pesquisador = Agent(role='Pesquisador',
                    goal='Pesquisar informações sobre a gastronomia peruana deste ano 2024.',
                    backstory="""Você é um especialista em gastronomia peruana.""",
                    verbose=True,
                    memory=True,
                    allow_delegation=False,
                    llm=ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0.0),
                    tools=[DuckDuckGoSearchRun()]
                   )

escritor = Agent(role="Escritor",
                 goal="Escreva postagens de blog atraentes e envolventes sobre a gastronomia peruana deste ano 2024.",
                 backstory="Você é um escritor de postagens em um blog de Gastronomia, especializado em escrever sobre tópicos da comida peruana.",
                 verbose=True,
                 memory=True,
                 allow_delegation=True,
                 llm=ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0.0)
                 )

# 2. Criamos as tarefas para nossos Agentes:
task1 = Task(description='Responda apenas em Português pt-BR. Investiga as últimas tendências ou informações da gastronomia peruana.',
             agent=pesquisador,
             expected_output = "Um resumo das 3 notícias mais importantes da gastronomia peruana deste ano 2024."
            )

task2 = Task(description="Responda apenas em Português pt-BR. Escreve uma postagem atraente no blog de gastronomia com base nas últimas tendências da comida peruana.",
             agent=escritor,
             expected_output = """
                               A postagem no blog deve conter 3 parágrafos sobre as mais recentes tendências da gastronomia peruana do 2024.
                               Adiciona um Título que faça sentido com dita pesquisa.
                               """,
             output_file='Eddy-blog-Peru.md'  # Exemplo de personalização de saída
            )

# 3. Crew como um processo sequencial:
crew = Crew(
            agents=[pesquisador, escritor],
            tasks=[task1, task2],
            verbose=2,
            process=Process.sequential,
            #language='pt-BR',
            # language_file=None
           )

# 4. Iniciar a execução de crew:
result = crew.kickoff()

print(result)
print("\n\n")
#print(crew.usage_metrics)
