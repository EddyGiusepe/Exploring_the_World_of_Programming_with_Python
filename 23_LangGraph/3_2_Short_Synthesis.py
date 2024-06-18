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

# Usando LangSmith:
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"  # Eddy ---> https://smith.langchain.com/o/fc23d72c-9360-5a5f-affa-26c44b810011
LANGCHAIN_API_KEY="sua Key para o LangSmith"
LANGCHAIN_PROJECT="LangGraph_EddyGiusepe"


import asyncio
from langgraph.graph import END, MessageGraph
from typing import List, Sequence
from langgraph.graph import MessageGraph, END
from langchain_core.messages import BaseMessage, HumanMessage
from decouple import config
from langchain_openai import ChatOpenAI
from typing import List
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.document_loaders import UnstructuredFileLoader

# Carregar PDF ou Docx ou qualquer outro formato:
pdf_file = "/home/eddygiusepe/1_Eddy_Giusepe/Exploring_the_World_of_Programming_with_Python/22_PDF_and_Images_Content_Extraction_for_LLM/data/edital.pdf"

# Transformar o PDF em texto com UnstructuredFileLoader:
def extract_text_with_langchain_pdf(pdf_file):
    loader = UnstructuredFileLoader(pdf_file)
    documents = loader.load()
    pdf_pages_content = '\n'.join(doc.page_content for doc in documents)
    return pdf_pages_content

text = extract_text_with_langchain_pdf(pdf_file)
#breakpoint()

# Crio o PROMPT:
prompt = ChatPromptTemplate.from_messages(
    [
        (
"system",
"Você é um Editor de Conteúdo que analisa e sumariza documentos. Sua tarefa é fornecer resumos claros, objetivos e informativos de diferentes tipos de documentos."
" Seu resumo deve ser factual, baseando-se no documento original e abrangendo os aspectos mais importantes dele."
" Fornecerei a você um documento e você fonecerá um resumo de dois parágrafos desse documento."
" Seja objetivo e evite opiniões pessoais."
" Se o usuário fizer críticas, responda com uma versão melhorada e adicione RESUMO seguido do título original do documento.",
        ),
        MessagesPlaceholder(variable_name="text"),
    ]
)

# Instanciar o modelo LLM:
llm = ChatOpenAI(model="gpt-4o", temperature=0, streaming=True) # "gpt-4o"   ou    "gpt-3.5-turbo-0125"

# Criar a função de geração:
generate = prompt | llm

# Criar a função de reflexão:
reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
"system",
"Você é um Especialista em Sumarização que analisa e dá sugestões detalhadas para melhorar o resumo fornecido."
" Revise cuidadosamente a análise do Editor de Conteúdo e avalie os parágrafos que precisam a ser melhorados."
" Seu objetivo é ajudar ao Editor de Conteúdo a tornar o resumo mais claro, factual e informativo."
" Verifique que o Editor de Conteúdo faça um resumo curto de apenas dois parágrafos.",
        ),
        MessagesPlaceholder(variable_name="text"),
    ]
)

reflect = reflection_prompt | llm

# Criar a função de geração de nós:
async def generation_node(state: Sequence[BaseMessage]):
    return await generate.ainvoke({"text": state})

# Criar a função de reflexão:
async def reflection_node(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    # Outras mensagens que precisamos ajustar:
    cls_map = {"ai": HumanMessage, "human": AIMessage}

    # A primeira mensagem é a solicitação original do usuário. Mantemos o mesmo para todos os nós:
    translated = [messages[0]] + [
        cls_map[msg.type](content=msg.content) for msg in messages[1:]
    ]
    res = await reflect.ainvoke({"text": translated})

    # Isso será tratado como um feedback para o gerador:
    return HumanMessage(content=res.content)

# Criar o grafo de mensagens:
builder = MessageGraph()
builder.add_node("generate", generation_node)
builder.add_node("reflect", reflection_node)
builder.set_entry_point("generate")

# Definir a condição para parar a geração:
def should_continue(state: List[BaseMessage]):
    if len(state) > 3:
        # Terminar após 2 iterações
        return END
    return "reflect"

# Adicionar as condições de parada:
builder.add_conditional_edges("generate", should_continue)
builder.add_edge("reflect", "generate")

# Compilar o grafo:
graph = builder.compile()

# Função para gerar respostas:
async def stream_responses():
    #last_content = None
    async for event in graph.astream([HumanMessage(content=text)]):
        print(event)
        print("---")
        if 'generate' in event:
            last_content = event['generate'].content  # Armazena o 'content' da mensagem 'generate'
    
    if last_content:
        print(last_content)  # Imprime o 'content' da última mensagem gerada
        type(last_content)

# Executar a função:
asyncio.run(stream_responses())
