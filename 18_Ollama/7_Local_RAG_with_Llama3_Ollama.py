#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Link de estudo ---> https://levelup.gitconnected.com/local-rag-with-llama3-instruct-ollama-305a7eb749cb

#initiating the ollama:
ollama serve && ollama run

# dwonloading the model:
ollama pull llama3-instruct
"""

# !pip install langchain-community==0.2.4 langchain==0.2.3 faiss-cpu==1.8.0 unstructured==0.14.5 unstructured[pdf]==0.14.5 transformers==4.41.2 sentence-transformers==3.0.1
import os
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

from langchain_community.llms import Ollama
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.vectorstores import FAISS
#from langchain.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings  
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA

# loading the LLM:
llm = Ollama(model="llama3:instruct",
             temperature=0
            )

# loading the document:
loader = UnstructuredPDFLoader("/home/eddygiusepe/2_EddyGiusepe_Estudo/Exploring_the_World_of_Programming_with_Python/24_crewAI/CHATGPT_Granularity_clustering.pdf")
documents = loader.load()

# create document chunks:
text_splitter = CharacterTextSplitter(separator="/n",
                                      chunk_size=1000,
                                      chunk_overlap=200)

text_chunks = text_splitter.split_documents(documents)

# loading the vector embedding model:
embeddings = HuggingFaceEmbeddings()

knowledge_base = FAISS.from_documents(text_chunks, embeddings)

# retrieval QA chain:
qa_chain = RetrievalQA.from_chain_type(llm,
                                       retriever=knowledge_base.as_retriever()
                                      )
print("\n")
# Exemplo 1:
question = "Responde apenas em Português: O documento fala sobre que?"
response = qa_chain.invoke({"query": question})
print(response["result"])

# Exemplo 2:
question = "O que é granularidade?"
response = qa_chain.invoke({"query": question})
print(response["result"])





