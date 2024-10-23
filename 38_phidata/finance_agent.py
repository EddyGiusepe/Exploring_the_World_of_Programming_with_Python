#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

=================
Agente Financeiro
=================

Github: https://github.com/phidatahq/phidata
"""
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
#openai.api_key  = os.environ['OPENAI_API_KEY']
#Eddy_key_openai  = os.environ['OPENAI_API_KEY']
#from openai import OpenAI
#client = OpenAI(api_key=Eddy_key_openai)

# Vamos criar outro agente que pode consultar dados financeiros:
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools

finance_agent = Agent(
    name="Agente Financeiro",
    role="Obtenha dados financeiros",
    model=OpenAIChat(id="gpt-4o-2024-08-06"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Sempre use tabelas para exibir dados"],
    markdown=True,
    show_tool_calls=True,
)

finance_agent.print_response("Compartilhe recomendações de analistas para NVDA", stream=True)
