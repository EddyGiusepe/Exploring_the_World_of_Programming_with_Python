#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
#openai.api_key  = os.environ['OPENAI_API_KEY']
#Eddy_key_openai  = os.environ['OPENAI_API_KEY']
#from openai import OpenAI
#client = OpenAI(api_key=Eddy_key_openai)
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

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Você é um pesquisador assistente de IA encarregado de pesquisar uma variedade de tópicos em um breve resumo de 2 parágrafos."
            " Gere a melhor pesquisa possível de acordo com a solicitação do usuário."
            " Se o usuário fizer críticas, responda com uma versão revisada de suas tentativas anteriores.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0, streaming=True) # "gpt-4o"   ou    "gpt-3.5-turbo-0125"

generate = prompt | llm


reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Você é um pesquisador experto"
            " Forneça recomendações detalhadas, incluindo solicitações de comprimento, profundidade, estilo, etc."
            " a um pesquisador assistente para ajudar a melhorar sua pesquisa",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

reflect = reflection_prompt | llm


async def generation_node(state: Sequence[BaseMessage]):
    return await generate.ainvoke({"messages": state})


async def reflection_node(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    # Outras mensagens que precisamos ajustar:
    cls_map = {"ai": HumanMessage, "human": AIMessage}

    # A primeira mensagem é a solicitação original do usuário. Mantemos o mesmo para todos os nós:
    translated = [messages[0]] + [
        cls_map[msg.type](content=msg.content) for msg in messages[1:]
    ]
    res = await reflect.ainvoke({"messages": translated})

    # Isso será tratado como um feedback para o gerador:
    return HumanMessage(content=res.content)


builder = MessageGraph()
builder.add_node("generate", generation_node)
builder.add_node("reflect", reflection_node)
builder.set_entry_point("generate")


def should_continue(state: List[BaseMessage]):
    if len(state) > 3:
        # Terminar após 2 iterações
        return END
    return "reflect"


builder.add_conditional_edges("generate", should_continue)
builder.add_edge("reflect", "generate")
graph = builder.compile()


async def stream_responses():
    async for event in graph.astream(
        [
            HumanMessage(
                content="Pesquisa sobre o País Perú"
            )
        ],
    ):
        print(event)
        print("---")


asyncio.run(stream_responses())
