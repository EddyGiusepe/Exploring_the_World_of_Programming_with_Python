#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
import requests
import json
import sys 

payload ={
    "model": "llama3.1:8b",
    "messages":[
        {"role":"assistant",
         "content":"""Eres um especialista em Análise de vibração, Manutenção preditiva e monitoramento de Ativos. \
                      Sua tarefa é dar Insights relevantes sobre dita área. A sua resposta deve ter 300 caracteres
                      como máximo.
                   """
        },
        {"role":"user","content": "Como posso prevenir um desgaste de Rolamentos nas minhas máquinas?"},
    ],
    "format":"json",
    "stream":False, # True ou False
    "options": {
        #"seed": 123,
        "temperature": 0.0
  }
}

response= requests.post(
    "http://localhost:11434/api/chat",
    json= payload
)

print(response.json())

#print('-------------------------------------')
#print(response.json()['message']['content'])
