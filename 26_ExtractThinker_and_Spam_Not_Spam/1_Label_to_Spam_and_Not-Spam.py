#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Estudar os seguintes Links
==========================
* https://github.com/enoch3712/ExtractThinker

* https://python.useinstructor.com/hub/
* https://python.useinstructor.com/hub/single_classification/
* https://github.com/jxnl/instructor/
"""
from pydantic import BaseModel, Field
from typing import Literal
from openai import OpenAI
import instructor

# Apply the patch to the OpenAI client
# enables response_model keyword
client = instructor.from_openai(OpenAI())


class ClassificationResponse(BaseModel):
    label: Literal["SPAM", "NOT_SPAM"] = Field(
        ...,
        description="O rótulo da classe prevista.",
    )


def classify(data: str) -> ClassificationResponse:
    """Perform single-label classification on the input text."""
    return client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_model=ClassificationResponse,
        messages=[
            {
                "role": "user",
                "content": f"Classifique o seguinte texto: {data}",
            },
        ],
    )


if __name__ == "__main__":
    # for text, label in [
    #     ("Olá, Jasão! Você é incrível", "NOT_SPAM"),
    #     ("Sou um príncipe nigeriano e preciso da sua ajuda.", "SPAM"),
    # ]:
        prediction = classify("""Olá,
Você está procurando uma maneira de ganhar dinheiro extra? Temos a solução perfeita para você!
Apresentamos o nosso novo programa de investimento que pode lhe render milhares de reais em apenas algumas semanas. Basta investir uma pequena quantia inicial e você verá seus lucros crescerem exponencialmente.
Não perca essa oportunidade única! Clique aqui para saber mais [LINK SUSPEITO].
Atenciosamente,
Equipe de Investimentos XYZ
Este é um exemplo clássico de spam. Algumas características que o identificam como tal:
Promessas de ganhos rápidos e fáceis
Linguagem exagerada e sensacionalista
Convite para clicar em um link suspeito
Remetente desconhecido ou com nome genérico
Ausência de informações de contato legítimas
Mensagens como essa geralmente têm o objetivo de enganar as pessoas, induzindo-as a clicar em links maliciosos ou a fornecer informações pessoais. É importante sempre desconfiar de ofertas milagrosas e nunca clicar em links de remetentes desconhecidos.""")
        # assert prediction.label == label
        # print(f"Text: {text}, Predicted Label: {prediction.label}")
        #> Text: Hey Jason! You're awesome, Predicted Label: NOT_SPAM
        #> Text: I am a nigerian prince and I need your help., Predicted Label: SPAM
        print(prediction)












