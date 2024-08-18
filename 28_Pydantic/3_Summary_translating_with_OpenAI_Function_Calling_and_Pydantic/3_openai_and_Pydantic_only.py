#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Structured Outputs
==================
Neste script estudamos o tutorial da OpenAI para 
Saídas Estruturadas a qual usa pydantic.

Link de estudo --> https://platform.openai.com/docs/guides/structured-outputs/introduction
"""
from dotenv import find_dotenv, load_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
from openai import OpenAI
client = OpenAI()


from pydantic import BaseModel, Field

class CalendarEvent(BaseModel):
    name: str
    date: str = Field(..., description="O dia da semana que será o evento")
    participants: list[str] = Field(..., description="Nome dos participants numa lista")

completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "Você é um assistente que extrai informações de um texto fornecido."},
        {"role": "user", "content": "Alice e Bob vão a uma feira de ciências na sexta-feira."},
    ],
    temperature=0,
    response_format=CalendarEvent,
)


event = completion.choices[0].message.parsed
print(type(event))
print(event)
print("")
print(event.name)
