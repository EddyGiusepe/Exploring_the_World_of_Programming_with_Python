#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

crewAI
======
Aqui realizo um exemplo, de uso Básico, do Framework 🤖 crewAI de ponta
para orquestrar agentes de IA autônomos e role-playing. Ao promover a inteligência
colaborativa, a 🤖 CrewAI capacita os agentes a trabalharem juntos de forma integrada,
lidando com tarefas complexas.
Aqui estou usando uma classe que herda o Agent de crewAI.

Install
=======
$ pip install crewai
$ pip install 'crewai[tools]'
"""
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

class MeuAgente(Agent): # A classe MeuAgente herda de Agent
    def __init__(self, nome, papel, ferramentas=None):
        super().__init__(
            name=nome,
            role=papel,
            goal="Realizar tarefas específicas conforme solicitado",
            backstory="""Você é um especialista em Análise de vibração, Manutenção preditiva e monitoramento de ativos industriais.
                         Su aterfa é responder as perguntas do usuário.
                         Forneça uma resposta com apenas 250 caracteres como máximo.
                      """,
            verbose=True,
            allow_delegation=False,
            llm=ChatOpenAI(model_name="gpt-4o-2024-08-06", temperature=0.0), # gpt-4o-2024-08-06    ou    gpt-4o-mini
            tools=ferramentas or []
        )

    def executar_tarefa(self, descricao_tarefa):
        tarefa = Task(
            description=descricao_tarefa,
            agent=self, # 'self' refere-se à instância atual da classe MeuAgente
            expected_output="Uma resposta concisa, informativa e factual."
        )
        resultado = self.execute_task(tarefa) # O método execute_task() vem da classe pai Agent
        return resultado



# Testando o meu agente:
if __name__ == "__main__":
    agente = MeuAgente("Especialista em Análise vibração e Manutenção Preditiva", 
                       "Experto em Análise de vibração e Manutenção Preditiva")
    
    resultado = agente.executar_tarefa("O que é BPFO e quando ocurre isso?")
    print(resultado)
