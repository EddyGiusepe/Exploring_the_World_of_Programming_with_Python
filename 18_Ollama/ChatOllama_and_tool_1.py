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
from typing import List

from langchain_core.tools import tool
from langchain_ollama import ChatOllama


@tool
def validate_user(user_id: int, addresses: List[str]) -> bool:
    """Valide o usuário usando endereços históricos.

    Args:
        user_id (int): o ID do usuário.
        addresses (List[str]): Endereços anteriores como uma lista de strings.
    """
    return True


llm = ChatOllama(model="llama3.1:8b", # llama3.1:8b    ou    phi3:3.8b
                 temperature=0,
                ).bind_tools([validate_user]) # Ferramentas de vinculação, o LLM pode usar essa ferramenta (ou seja ganha capacidade de chamar a função)

result = llm.invoke(
    """
    Você poderia validar o usuário 123?
    
    Eles moravam anteriormente em 123 Fake St em Boston MA e 234 Pretend Boulevard em Houston TX.
    """
)
print(result.tool_calls)