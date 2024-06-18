#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

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
pdf_file1 = "/home/eddygiusepe/1_Eddy_Giusepe/Exploring_the_World_of_Programming_with_Python/22_PDF_and_Images_Content_Extraction_for_LLM/data/edital.pdf"
pdf_file2 = "/home/eddygiusepe/1_Eddy_Giusepe/Exploring_the_World_of_Programming_with_Python/22_PDF_and_Images_Content_Extraction_for_LLM/data/minuta_contrato.pdf"


# Transformar o PDF em texto com UnstructuredFileLoader:
def extract_text_with_langchain_pdf(pdf_file):
    loader = UnstructuredFileLoader(pdf_file)
    documents = loader.load()
    pdf_pages_content = '\n'.join(doc.page_content for doc in documents)
    return pdf_pages_content

text1 = extract_text_with_langchain_pdf(pdf_file1)
text2 = extract_text_with_langchain_pdf(pdf_file1)

# Crio o PROMPTs para analisar os dois PDFs:
prompt1 = ChatPromptTemplate.from_messages(
    [
        (
"system",
"Você é um pesquisador Assistente que análisa documentos e está encarregado de analisar cuidadosamente esses tipos de documentos."
" Gere uma análise detalhada e explícita do contrato ou documento jurídico, incluindo uma explicação clara do significado e das implicações de cada cláusula."
" Inclua informações sobre as principais obrigações e direitos de cada parte, prazos, penalidades ou riscos e quaisquer ambiguidades ou informações conflitantes."
" Se você encontrar informações ambíguas ou conflitantes, indique claramente quais são e forneça uma explicação das possíveis interpretações."
" Se o usuário fizer críticas, responda com uma versão melhorada e bem detalhada de cada ponto analisado.",
        ),
        MessagesPlaceholder(variable_name="text1"),
    ]
)

prompt2 = ChatPromptTemplate.from_messages(
    [
        (
"system",
"Você é um pesquisador Assistente que análisa documentos e está encarregado de analisar cuidadosamente esses tipos de documentos."
" Gere uma análise detalhada e explícita do contrato ou documento jurídico, incluindo uma explicação clara do significado e das implicações de cada cláusula."
" Inclua informações sobre as principais obrigações e direitos de cada parte, prazos, penalidades ou riscos e quaisquer ambiguidades ou informações conflitantes."
" Se você encontrar informações ambíguas ou conflitantes, indique claramente quais são e forneça uma explicação das possíveis interpretações."
" Se o usuário fizer críticas, responda com uma versão melhorada e bem detalhada de cada ponto analisado.",
        ),
        MessagesPlaceholder(variable_name="text2"),
    ]
)

# Instanciar o modelo LLM:
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0, streaming=True) # "gpt-4o"   ou    "gpt-3.5-turbo-0125"

# Crio as funções de geração:
generate1 = prompt1 | llm
generate2 = prompt2 | llm

# Crio as funções de reflexão:
reflection_prompt1 = ChatPromptTemplate.from_messages(
    [
        (
"system",
"Você é um experto Analista jurídico encarregado de fornecer recomendações para melhorar a análise de um contrato ou documento jurídico realizado por um pesquisador assistente."
" Revise cuidadosamente a análise atual do pesquisador assistente e avalie os pontos a ser melhorado."
" Forneça recomendações detalhadas para melhorar a clareza, precisão, abrangência da análise, riscos, penalidades ou qualquer informação relevante dentro do documento."
" Forneça exemplos específicos de como a análise pode ser melhorada em termos de clareza, precisão, abrangência, possíveis riscos, etc."
" Adicione, entre aspas, os pontos a melhorar e suas recomendações.",
        ),
        MessagesPlaceholder(variable_name="text1"),
    ]
)

reflection_prompt2 = ChatPromptTemplate.from_messages(
    [
        (
"system",
"Você é um experto Analista jurídico encarregado de fornecer recomendações para melhorar a análise de um contrato ou documento jurídico realizado por um pesquisador assistente."
" Revise cuidadosamente a análise atual do pesquisador assistente e avalie os pontos a ser melhorado."
" Forneça recomendações detalhadas para melhorar a clareza, precisão, abrangência da análise, riscos, penalidades ou qualquer informação relevante dentro do documento."
" Forneça exemplos específicos de como a análise pode ser melhorada em termos de clareza, precisão, abrangência, possíveis riscos, etc."
" Adicione, entre aspas, os pontos a melhorar e suas recomendações.",
        ),
        MessagesPlaceholder(variable_name="text2"),
    ]
)

reflect1 = reflection_prompt1 | llm
reflect2 = reflection_prompt2 | llm

# Crio as funções de geração de nós para cada PDF:
async def generation_node1(state: Sequence[BaseMessage]):
    return await generate1.ainvoke({"text1": state})

async def generation_node2(state: Sequence[BaseMessage]):
    return await generate2.ainvoke({"text2": state})

# Crio as funções de reflexão para cada PDF:
async def reflection_node1(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    # Outras mensagens que precisamos ajustar:
    cls_map = {"ai": HumanMessage, "human": AIMessage}
    # A primeira mensagem é a solicitação original do usuário. Mantemos o mesmo para todos os nós:
    translated = [messages[0]] + [
        cls_map[msg.type](content=msg.content) for msg in messages[1:]
    ]
    res = await reflect1.ainvoke({"text1": translated})
    # Isso será tratado como um feedback para o gerador:
    return HumanMessage(content=res.content)

async def reflection_node2(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    # Outras mensagens que precisamos ajustar:
    cls_map = {"ai": HumanMessage, "human": AIMessage}
    # A primeira mensagem é a solicitação original do usuário. Mantemos o mesmo para todos os nós:
    translated = [messages[0]] + [
        cls_map[msg.type](content=msg.content) for msg in messages[1:]
    ]
    res = await reflect2.ainvoke({"text2": translated})
    # Isso será tratado como um feedback para o gerador:
    return HumanMessage(content=res.content)

# Crio os grafos de mensagens:
builder = MessageGraph()
builder.add_node("generate1", generation_node1)
builder.add_node("reflect1", reflection_node1)
builder.add_node("generate2", generation_node2)
builder.add_node("reflect2", reflection_node2)
builder.set_entry_point("generate1")

# Definir a condição para parar a geração:
def should_continue(state: List[BaseMessage]):
    if len(state) > 2:
        # Terminar após 2 iterações
        return END
    return "reflect1"

# Adicionar as condições de parada:
builder.add_conditional_edges("generate1", should_continue)
builder.add_edge("reflect1", "generate2")
builder.add_edge("reflect2", "generate1")
builder.add_edge("generate2", "reflect2")

# Compilar o grafo:
graph = builder.compile()

# Função para gerar respostas:
async def stream_responses():
    #last_content = None
    async for event in graph.astream([HumanMessage(content=text1)]):
        print(event)
        print("---")
        if 'generate1' in event:
            last_content = event['generate1'].content  # Armazena o 'content' da mensagem 'generate'
        elif "generate2" in event:
            last_content = event['generate2'].content
        if last_content:
            print(last_content)
    # if last_content:
    #     print(last_content)  # Imprime o 'content' da última mensagem gerada
        

# Executar a função:
asyncio.run(stream_responses())
