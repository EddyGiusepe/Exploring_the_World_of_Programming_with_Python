#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Para ver um exemplo mais detalhado, peça acesso ao meu repositório do HuggingFace --> https://huggingface.co/spaces/EddyGiusepe/Predictive_Maintenance_of_Machines/blob/main/7_Predictive_Maintenance_with_crewAI.py
"""
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
import json

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file


class MeuAgente(Agent):
    def __init__(self, nome, papel, ferramentas=None):
        super().__init__(
            name=nome,
            role=papel,
            goal="Analyze vibration data and predictive maintenance",
            backstory=
            """
            You are an expert in vibration analysis, predictive maintenance and industrial asset monitoring. 
            Your task is to generate concise, informative and factual summaries about the conditions detected 
            in the asset (machine), based on the Input provided by the user.
            """,
            verbose=False,
            allow_delegation=False,
            llm=ChatOpenAI(model_name="gpt-4o-2024-08-06", temperature=0.0),
            tools=ferramentas or []
        )

    def analisar_dados(self, dados_json):
        # Converte para dicionário se for uma string JSON
        if isinstance(dados_json, str):
            try:
                dados = json.loads(dados_json)
            except json.JSONDecodeError:
                return "Error: The provided JSON is invalid."
        else:
            dados = dados_json

        # Cria uma descrição da tarefa com os dados JSON:
        descricao_tarefa = f"""
        Parse the following user input (delimited by ####):

        ####
        {json.dumps(dados, indent=2)}
        ####

        and provide a factual inspection summary limiting your answer to 250 characters.
        Response:
        """
        
        tarefa = Task(
            description=descricao_tarefa,
            agent=self,
            expected_output="A concise and relevant insight based on the data provided.."
        )
        return self.execute_task(tarefa)

if __name__ == "__main__":
    agente = MeuAgente("Specialist in Vibration Analysis and Predictive Maintenance",
                       "Specialist in Vibration Analysis, Predictive Maintenance and Asset Monitoring"
                      )
    
    # Qualquer JSON relacionado à manutenção preditiva:
    dados_json = '''
            {     "detectable_senses": ["touch", "hearing", "sight"]
            }     
                 '''
    
    resultado = agente.analisar_dados(dados_json)
    print(resultado)
