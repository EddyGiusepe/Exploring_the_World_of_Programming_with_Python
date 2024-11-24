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
# Vamos começar construindo um agente simples que pode pesquisar na web:
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.agent import Agent, RunResponse
from phi.utils.pprint import pprint_run_response
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.lancedb import LanceDb, SearchType
from phi.playground import Playground, serve_playground_app
import json
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

from colorama import init, Fore, Style
init(autoreset=True)
import logging
logging.basicConfig(level=logging.INFO)

def interactive_web_search():
    web_agent = Agent(name="Agente Web",
                      role="Pesquise informações na web",
                      model=OpenAIChat(id="gpt-4o-2024-08-06"),
                      tools=[DuckDuckGo()],
                      markdown=True,
                      show_tool_calls=True,
                      debug_mode=False
                     )

    while True:
        logging.info(f"{Fore.GREEN}Digite sua pergunta (ou 'sair' para encerrar): {Style.RESET_ALL}")
        query = input()
        if query.lower() == "sair":
            logging.info(f"{Fore.RED}Encerrando o agente de pesquisa na web.{Style.RESET_ALL}")
            break
        response: RunResponse = web_agent.run(query) # Run agent and return the response as a variable
        print(response.content)



if __name__ == "__main__":
    interactive_web_search()
