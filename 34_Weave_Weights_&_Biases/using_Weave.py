#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

=====
Weave
=====
Weave é um kit de ferramentas para desenvolver aplicativos de IA generativa, criado pela Weights & Biases!


Weave ---> https://github.com/wandb/weave
"""
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
#openai.api_key  = os.environ['OPENAI_API_KEY']
#Eddy_key_openai  = os.environ['OPENAI_API_KEY']
#from openai import OpenAI

import weave
import json
from openai import OpenAI

@weave.op()
def extract_fruit(sentence: str) -> dict:
    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "Você receberá dados não estruturados e sua tarefa é analisá-los em um dicionário JSON com frutas, cores e sabores como chaves."
        },
        {
            "role": "user",
            "content": sentence
        }
        ],
        temperature=0.4,
        response_format={ "type": "json_object" }
    )
    extracted = response.choices[0].message.content
    return json.loads(extracted)

weave.init('eddy-exemplo-weave')



sentence = "Há muitas frutas que foram encontradas no planeta recentemente descoberto Goocrux. Há neoskizzles que crescem lá, que são roxos e têm gosto de doce."
response = extract_fruit(sentence)
print(response)
