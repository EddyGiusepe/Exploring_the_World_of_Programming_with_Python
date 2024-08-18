#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Link de estudo ---> https://github.com/jxnl/instructor
"""
from dotenv import find_dotenv, load_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
from openai import OpenAI
# client = OpenAI()

import instructor
from pydantic import BaseModel
from openai import OpenAI


# Defina a estrutura de saída desejada:
class UserInfo(BaseModel):
    name: str
    age: int


# Patch the OpenAI client:
client = instructor.from_openai(OpenAI())

# Extract structured data from natural language
user_info = client.chat.completions.create(
    model="gpt-4o",
    response_model=UserInfo,
    messages=[
            {
                "role": "system",
                "content": """
                        Você é um especialista em Reconhecimento de Entidades (NER). Basicamente, você \
                        deve identificar o NOME e a IDADE no texto fornecido.
                        """
            },
            {"role": "user", "content": """A Karina e Brasileira e tem 26 anos de idades."""}
        ],
)


print(user_info.name)

print(user_info.age)

