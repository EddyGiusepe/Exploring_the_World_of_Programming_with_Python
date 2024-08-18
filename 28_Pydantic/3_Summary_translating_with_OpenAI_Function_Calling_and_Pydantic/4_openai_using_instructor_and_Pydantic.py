#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Neste script usamos instructor e pydantic para obter uma 
Saída Estruturada.

Link de estudo ---> https://github.com/jxnl/instructor
"""
from dotenv import find_dotenv, load_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

import instructor
from pydantic import BaseModel, Field
from typing import List
from openai import OpenAI
# client = OpenAI()

class Question(BaseModel):
    question: str = Field(..., description="The quiz question text")
    options: List[str] = Field(..., description="Multiple choice options")
    correct_answer: int = Field(..., description="Index of the correct answer in options list")


class Quiz(BaseModel):
    topic: str = Field(..., description="The topic of the quiz")
    questions: List[Question] = Field(..., description="List of questions in the quiz")


# Patch the OpenAI client:
client = instructor.from_openai(OpenAI())


def generate_quiz(prompt_question):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system",
                    "content": """
                            Você é um mecanismo de geração de quiz, especializado em promover
                            a compreensão em alunos, dada uma fonte de conteúdo a ser estudada.
                            Você será alimentado com conteúdo como artigos ou trabalhos científicos
                            e produzirá questionários com o objetivo de obter a compreensão completa do material. 
                            """
                },
                {"role": "user", "content": f"""{prompt_question}"""}
            ],
        temperature=0,
        response_model=Quiz
    )

    return response

# Source
prompt = """
Quero que você faça o seguinte:
1. Identifique o tópico principal dos seguintes artigos:
'''
PNAS logo
ARTICLES 
FRONT MATTER
AUTHORS
RESEARCH ARTICLE
PSYCHOLOGICAL AND COGNITIVE SCIENCES
OPEN ACCESS
SHARE ON

A first model-independent radial BAO constraint from the final BOSS sample

Authors: Valerio Marra, Eddy G. Chirinos Isidro

Abstract: Using almost one million galaxies from the final Data Release 12 of the SDSS's Baryon Oscillation Spectroscopic Survey, we have obtained, albeit with low significance, a first model-independent determination of the radial BAO peak with 9% error: . In order to obtain this measurement, the radial correlation function was computed in 7,700 angular pi… ▽ More
Submitted 3 June, 2019; v1 submitted 31 August, 2018; originally announced August 2018.

Comments: 9 pages, 8 figures; major revision: improved analysis and BOSS mocks. Version accepted for publication in MNRAS

Journal ref: MNRAS 487, 3419-3426 (2019)
'''
2. Crie um quiz com 5 perguntas que giram em torno deste tópico principal e podem ser respondidas simplesmente lendo e
entendendo cuidadosamente o artigo. Uma dessas perguntas deve verificar se o aluno entendeu as ideias principais
testando se o aluno consegue transferir seu conhecimento em um contexto diferente dos descritos no conteúdo.
Output:
"""

quiz_output = generate_quiz(prompt)

print(quiz_output)

print("\n\n")
for q in quiz_output.questions:
    print(q.question)
    for i, o in enumerate(q.options):
        print(i, o)
    print("Correct answer:", q.correct_answer)