#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

=====================
Agentes de raciocínio
=====================
O raciocínio ajuda os agentes a trabalhar em um problema
passo a passo, retrocedendo e corrigindo conforme necessário.
Vamos dar ao agente de raciocínio uma tarefa simples na qual
o gpt-4o falha.

Github: https://github.com/phidatahq/phidata
"""
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
#openai.api_key  = os.environ['OPENAI_API_KEY']
#Eddy_key_openai  = os.environ['OPENAI_API_KEY']
#from openai import OpenAI


from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.cli.console import console

regular_agent = Agent(model=OpenAIChat(id="gpt-4o"), markdown=True)

reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o-2024-08-06"),
    reasoning=True,
    markdown=True,
    structured_outputs=True,
    reasoning_min_steps=1,
    reasoning_max_steps=2,
    #debug_mode=True
)

task = "Quantos 'r' existem na palavra 'supercalifragilisticexpialidociousr'?" #"Achar o lado do quadrado em que o número que dá a área excede o número que dá o perímetro de 5" # Respotas é  5     #"Quantos 'r' existem na palavra 'supercalifragilisticexpialidocious'?"

console.rule("[bold green]Regular Agent[/bold green]")
regular_agent.print_response(task, stream=True)
print("")
console.rule("[bold yellow]Reasoning Agent[/bold yellow]")
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
