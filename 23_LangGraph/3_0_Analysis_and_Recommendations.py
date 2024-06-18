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
"Você é um pesquisador Assistente que análisa documentos e está encarregado de analisar cuidadosamente esses tipos de documentos."
" Gere uma análise detalhada e explícita do contrato ou documento jurídico, incluindo uma explicação clara do significado e das implicações de cada cláusula."
" Inclua informações sobre as principais obrigações e direitos de cada parte, prazos, penalidades ou riscos e quaisquer ambiguidades ou informações conflitantes."
" Se você encontrar informações ambíguas ou conflitantes, indique claramente quais são e forneça uma explicação das possíveis interpretações."
" Verifique se o contrato ou documento jurídico está em conformidade com as leis e regulamentações brasileiras, incluindo ISO (International Organization for Standardization), Normas, leis de licitação e contratos relevantes, etc."
" Inclua numeração na sua análise."
" Se o usuário fizer críticas, responda com uma versão melhorada e bem detalhada de cada ponto analisado.",
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
"Você é um experto Analista jurídico encarregado de fornecer recomendações para melhorar a análise de um contrato ou documento jurídico realizado por um pesquisador assistente."
" Revise cuidadosamente a análise atual do pesquisador assistente e avalie os pontos a ser melhorado."
" Forneça recomendações detalhadas para melhorar a precisão, abrangência da análise, possíveis riscos, penalidades ou qualquer informação relevante dentro do documento."
" Adicione, entre aspas, os pontos a melhorar, recomendações, etc."
" Verifique se a análise inclui numeração, informações sobre ISO, leis de licitação e contratos relevantes do Brasil e forneça recomendações para melhorar a abrangência da análise."
" Forneça sugestões de como melhorar a análise para que ela seja mais precisa e clara, considerando as leis, Normas e regulamentações brasileiras.",
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
        

# Executar a função:
asyncio.run(stream_responses())
