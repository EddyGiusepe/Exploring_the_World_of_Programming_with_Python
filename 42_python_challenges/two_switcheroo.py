#! /usr/bin/env python3
"""
Senior Data Scientist/AI Engineering.: Dr. Eddy Giusepe Chirinos Isidro

---------------------------------
Descrição do Problema: Switcheroo
---------------------------------
Dada uma string composta pelas letras a, b e/ou c,
troque a posição das letras a e b (mude a para b e vice-versa).
Qualquer ocorrência de c deve ser mantida sem alteração.

Exemplos:
    'acb'       -->  'bca'
    'aabacbaa'  -->  'bbabcabb'
"""


def switcheroo(string: str) -> str:
    text = string.replace("a", "x").replace("b", "a").replace("x", "b")
    return text


if __name__ == "__main__":
    print(switcheroo("acb"))
    print(switcheroo("aabacbaa"))
    print(switcheroo("aaacbbbcaaaccca"))
