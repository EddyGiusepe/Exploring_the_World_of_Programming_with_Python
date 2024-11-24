#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

=========================
Agente de pesquisa na Web
=========================

Github: https://github.com/phidatahq/phidata


O que é phidata?
================
Phidata é um Framework para construção de sistemas de agentes, use o Phidata para:

* Crie agentes inteligentes com memória, conhecimento, ferramentas e raciocínio.
* Execute esses agentes como um aplicativo de software (com um banco de dados, vectordb e API).
* Monitore, avalie e otimize seu sistema de agente.
"""
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.lancedb import LanceDb, SearchType
from phi.playground import Playground, serve_playground_app
from phi.tools.duckduckgo import DuckDuckGo

import json
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
#openai.api_key  = os.environ['OPENAI_API_KEY']
#Eddy_key_openai  = os.environ['OPENAI_API_KEY']
#from openai import OpenAI
#client = OpenAI(api_key=Eddy_key_openai)

# Vamos começar construindo um agente simples que pode pesquisar na web:
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.agent import Agent, RunResponse
from phi.utils.pprint import pprint_run_response

web_agent = Agent(
    name="Agente Web",
    role="Pesquise informações na web",
    model=OpenAIChat(id="gpt-4o-2024-08-06"),
    tools=[DuckDuckGo()],
    markdown=True,
    show_tool_calls=True,
    debug_mode=False
)

#web_agent.print_response("Quem foram os ganhadores do prêmio Nobel de Física do 2024?", stream=True, show_full_reasoning=True)

# Run agent and return the response as a variable:
response: RunResponse = web_agent.run("Quem foram os ganhadores do prêmio Nobel de Física do 2024?")

# # Print the response in markdown format:
# pprint_run_response(response, markdown=True)

assistant_message = response.content 
print(assistant_message)

