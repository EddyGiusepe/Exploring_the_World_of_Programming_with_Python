#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate


llm = Ollama(model = "phi3:3.8b", temperature=0)

prompt_template = PromptTemplate.from_template("Explique {topic} como se eu tivess {number} anos.")

chain = prompt_template | llm


response = print(chain.invoke({"topic":"conte uma piada",
                               "number": "5"
                              })
                )

print(response)
