#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
from datetime import datetime
from pydantic import BaseModel, PositiveInt


class User(BaseModel):
    id: int  
    name: str = 'John Doe'  
    signup_ts: datetime | None  
    tastes: dict[str, PositiveInt]  


external_data = {'id': 123,
                 'signup_ts': '2019-06-01 12:22',  
                 'tastes': {'wine': 9,
                           b'cheese': 7, # A chave aqui são bytes, mas o Pydantic cuidará de convertê-los em uma string. 
                            'cabbage': '1', # Da mesma forma, o Pydantic converterá a string '1' para um inteiro 1.
                           },
                }

user = User(**external_data) # Aqui criamos uma instância de 'User' passando nossos dados externos para 'User' como argumentos de palavra-chave

print(user.id) # Podemos acessar campos como atributos do modelo
print()
print(user)
print()
print(user.model_dump()) # Podemos converter o modelo em um dicionário com model_dump()
