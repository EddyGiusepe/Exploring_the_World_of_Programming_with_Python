#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Sumarização - Tradução - Tom - Sentimento - Idioma
==================================================
Neste script usamos a API da OpenAI para sumarizar e traduzir
um texto. Ademais, pedimos ao LLM inferir outras saídas. 
"""
import json

from dotenv import find_dotenv, load_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
from openai import OpenAI
client = OpenAI()


# Usando cores para a saída do Terminal:
YELLOW = "\033[0;33m"
GREEN = "\033[0;32m"
WHITE = "\033[0;37m"
RED = "\033[0;31m"
BLUE = "\033[0;34m"
RESET= "\033[m"

text = f"""
        Você deve expressar o que deseja que um modelo faça \
        fornecendo instruções que sejam tão claras e \
        específicas quanto possível. \
        Isso guiará o modelo em direção à saída desejada, \
        e reduzirá as chances de receber respostas irrelevantes \
        ou incorretas. Não confunda escrever um \
        prompt claro com escrever um prompt curto. \
        Em muitos casos, prompts mais longos fornecem mais clareza \
        e contexto para o modelo, o que pode levar a \
        saídas mais detalhadas e relevantes.
        """

prompt = f"""
          Texto: ```{text}```
          """

class Summarize_and_Translate:
    def __init__(self, model="gpt-4o", quantity_of_characters=200):
      self.model = model
      self.quantity_of_characters = quantity_of_characters

    def summarize_translate(self, prompt: str) -> dict:
        response = client.chat.completions.create(
            model=self.model, # "gpt-4o"   ou  "gpt-4o-mini"  ou  "gpt-3.5-turbo-0125"
            messages=[
            {
                "role": "system",
                "content": f"""
                        Você é um especialista em sumarizar e traduzir textos de diferentes idiomas. A sumarização deve \
                        ser clara, factual e informativa, baseada SOMENTE no texto fornecido. Seja breve, objetivo, \
                        evite opiniões pessoais e limite-se a {self.quantity_of_characters} caracteres.
                        """
            },
            {"role": "user", "content": prompt}
        ],
            temperature=0,
            functions=[{"name": "summarization_and_translation",
                        "description": """Resume o texto fornecido. Traduz o texto resumido ao Espanhol. Ademais, identifica o tom, sentimento e o idioma do texto que foi resumido.""",
                        "parameters": {"type": "object",
                                    "properties": {"summary": {"type": "string",
                                                               "description": "Resume o texto fornecido."
                                                              },
                                                   "translation": {"type": "string",
                                                               "description": "Traduz ao Espanhol (es-ES) o texto resumido ."
                                                              },
                                                    "tone": {"type": "string",
                                                            "description": "Identifica tom do texto resumido."
                                                            },
                                                    "sentiment": {"type": "string",
                                                                    "description": "Identifica o sentimento do texto resumido."
                                                                },
                                                    "language": {"type": "string",
                                                                "description": "Identifica o idioma da tradução."
                                                                }
                                                    },
                                        "required": ["summary", "translation", "tone", "sentiment", "language"]
                                    }
                    }
                    ],       
            function_call={"name": "summarization_and_translation"}         
                                                )
        json_response = json.loads(response.choices[0].message.function_call.arguments)
        #json_response = response
        return json_response



if __name__ == "__main__":
    print("")
    # Instanciando a minha classe:
    summarize_and_translate = Summarize_and_Translate(model="gpt-4o", quantity_of_characters=200)

    # Printando a saída do RESUMO e TRADUÇÃO:
    sumarizar_e_traduzir = summarize_and_translate.summarize_translate(prompt)
    print(f"{RED}{sumarizar_e_traduzir}{RESET}")

