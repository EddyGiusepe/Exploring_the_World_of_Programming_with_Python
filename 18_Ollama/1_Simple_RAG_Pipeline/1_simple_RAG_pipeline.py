#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
# 1. Importamos as bibliotecas necessárias:
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# 2. Variáveis de ambiente:
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
#openai.api_key  = os.environ['OPENAI_API_KEY']
#Eddy_key_openai  = os.environ['OPENAI_API_KEY']
#from openai import OpenAI
#client = OpenAI(api_key=Eddy_key_openai)

YELLOW = "\033[0;33m"
GREEN = "\033[0;32m"
WHITE = "\033[0;37m"
RED = "\033[0;31m"
RESET= "\033[m"

# Nosso Dataset será um PDF:  
DOC_PATH = "./CHATGPT Granularity clustering.pdf"

# Nome de nosso DB:
CHROMA_PATH = "eddy_DBChroma"

# Indexando nossos Dados
# ======================
loader = PyPDFLoader(DOC_PATH)
pages = loader.load()

# Split do Documento: 
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,
                                               chunk_overlap=50,
                                               separators=["\n\n", "\n", " ", ""]
                                              )
chunks = text_splitter.split_documents(pages)

# Nossos Modelo de Embeddings OpenAI:
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Carregando nossos Chunks como Vetores de Embeddings: 
db_chroma = Chroma.from_documents(chunks,
                                  embeddings,
                                  persist_directory=CHROMA_PATH,
                                  collection_name="eddy_DBChroma_Collection"
                                 )

"""
Processo de Recuperação e Geração
=================================
"""
query = "E qual é o objetivo do problema de classificação?" #"O que é granularidade de um Clustering?"

# Recuperar contexto: os 5 principais pedaços mais relevantes (mais próximos) do vetor de consulta
# (por padrão, Langchain está usando a métrica de distância do cosseno):
docs_chroma = db_chroma.similarity_search_with_score(query, k=2)
#print(docs_chroma)

# Gere uma resposta com base em determinada consulta do usuário e nas informações de contexto recuperadas:
context_text = "\n\n".join([doc.page_content for doc, _score in docs_chroma])
#print(context_text)

# Vamos a usar um PROMPT:
PROMPT_TEMPLATE = """
Responda à pergunta com base apenas no seguinte contexto:
{context}

Responda à pergunta com base no contexto acima: {question}.
Forneça uma resposta detalhada e completa.
Não justifique suas respostas.
Não forneça informações não mencionadas nas INFORMAÇÕES DE CONTEXTO.
Não diga “de acordo com o contexto” ou “mencionado no contexto” ou similar.
"""

# Carregar o contexto recuperado e a query do usuário no modelo de prompt:
prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

prompt = prompt_template.format(context=context_text, question=query)

# Chamamos ao modelo LLM para gerar a resposta com base no CONTEXTO e na QUERY fornecidos:
model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.0, streaming=True)

response_text = model.invoke(prompt)

print(response_text)
print("\n\n")

print(f"{GREEN}{response_text.content}{RESET}")