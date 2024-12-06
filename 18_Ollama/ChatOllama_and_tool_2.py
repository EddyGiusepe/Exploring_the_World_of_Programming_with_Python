#!/usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

ChatOllama
==========
Link de estudo --> https://python.langchain.com/docs/integrations/chat/ollama/

Aqui usamos o framework LangChain para interagir com o Ollama.

NOTA: 
====
Inicialize o 'ollama serve' antes de executar o script
"""
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2:3b", # llama3.1:8b    ou    phi3:3.8b   ou   llama3.2:3b
    temperature=0,
    # other params...
)

messages = [
    (
        "system",
        """Você é especialista em análise de vibração, manutenção preditiva e monitoramento de ativos industriais.
        """,
    ),
    ("human",
     """
     O que é a Transformada de Fourier e para que serve na Manutenção Preditiva?
     """),
]

ai_msg = llm.invoke(messages)

print(ai_msg)
print("--------------------------------")
print(ai_msg.content)
