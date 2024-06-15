#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
#openai.api_key  = os.environ['OPENAI_API_KEY']
#Eddy_key_openai  = os.environ['OPENAI_API_KEY']

#from openai import OpenAI
#client = OpenAI(api_key=Eddy_key_openai)

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.graph import END, MessageGraph

model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

# Inicializamos o Modelo:
graph = MessageGraph()
# Adicionamos um nó ao Graph:
graph.add_node("oracle", model)
# Adicionamos uma aresta do nó "oracle". 
graph.add_edge("oracle", END)
# Definimos "oracle"como ponto de entrada para o Graph:
graph.set_entry_point("oracle")
# Compilamos o Graph:
runnable = graph.compile()

# Executando:
res = runnable.invoke(HumanMessage("Quanto é: 3 + 6?"))
print(res[1].content)







