#! /usr/bin/env python3
"""
Senior Data Scientist/AI Engineering.: Dr, Eddy Giusepe Chirinos Isidro

-----------------------
Descrição do Problema:
-----------------------
Seus colegas programadores te compraram várias bebidas esta noite na forma de uma string.
Retorne uma string sugerindo quantos copos d'água você deve beber para não ter ressaca.

Exemplos:
    "1 beer"  -->  "1 glass of water"
    porque você bebeu um drinque padrão

    "1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"  -->  "10 glasses of water"
    porque você bebeu dez drinques padrão

Observação:
    Para simplificar, consideramos que qualquer bebida "numerada" conta como aquela
    quantidade de drinques padrão, independente do tipo da bebida.
    (ex: "2 beers" = 2 drinques padrão, "1 shot" = 1 drinque padrão)
"""


def hydrate(drink_string: str) -> str:

    part = ""
    done = []
    for i in drink_string:
        if i.isdigit():
            part = part + i
        elif part:  # "Se NÃO é dígito (else) E part não está vazio (if part)"
            done.append(int(part))
            part = ""

    return f"{sum(done)} glass{'es' if sum(done) != 1 else ''} of water"


if __name__ == "__main__":
    print(hydrate("1 beer 2 drinks"))  # "1 beer, 2 drinks, 3 beers"
