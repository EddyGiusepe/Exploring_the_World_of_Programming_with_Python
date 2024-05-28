#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from langchain_community.llms import Ollama

from langchain.prompts import PromptTemplate

import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
#openai.api_key  = os.environ['OPENAI_API_KEY']
#Eddy_key_openai  = os.environ['OPENAI_API_KEY']

#from openai import OpenAI
#client = OpenAI(api_key=Eddy_key_openai)

# pip install faiss-gpu ou pip install faiss-cpu
vectorstore = FAISS.from_texts(["Karina é uma experta em Machine Learning.",
                                "Os estudos da Karina foi no uso da API da OpenAI.",
                                "Ela estudou muito para chegar a ser uma Cientista de Dados."
                               ],
                               embedding=OpenAIEmbeddings(model="text-embedding-3-small")
)

retriever = vectorstore.as_retriever()
template = """Você é um assistente útil que responde as perguntas do Usuário. 
Use somente as seguintes partes do contexto recuperado para responder à pergunta.
Se você não sabe a resposta, apenas diga: 'Não sei', não tente inventar uma resposta.
Não precisa explicar detalhes de como foi gerada a resposta, só responda a pergunta
em base ao contexto fornecido.
{context}

Pergunta: {question}
Resposta, apenas, em Português:
"""

prompt = ChatPromptTemplate.from_template(template)
model = Ollama(model = "phi3:3.8b", temperature=0) # llama2:7b   phi3:3.8b

retrieval_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

response = retrieval_chain.invoke("A Karina é experta em que área?") # A Karina tem domínio em que área? Karina estudou que profissão?
print(response)
