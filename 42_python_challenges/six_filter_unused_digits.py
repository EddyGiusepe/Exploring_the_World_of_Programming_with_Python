#! /usr/bin/env python3
"""
Senior Data Scientist/AI Engineering.: Dr. Eddy Giusepe Chirinos Isidro

--------------------------------------------
Descrição do Problema: Filter unused digits
--------------------------------------------
Dada uma quantidade variável de argumentos inteiros (positivos),
retorne os dígitos que não aparecem em nenhum deles.

Observação:
    - Os dígitos da string resultante devem estar ordenados.

Exemplos:
    [12, 34, 56, 78]  -->  "09"
    [2015, 8, 26]     -->  "3479"
"""


def filter_unused_digits(lista: list[int]) -> str:
    "Retorna uma string ordenada com os dígitos de 0-9 que não aparecem"
    all_digits = set("0123456789")
    used_digits = {digit for number in lista for digit in str(number)}
    return "".join(sorted(all_digits - used_digits))


if __name__ == "__main__":
    print(filter_unused_digits([2, 0, 56, 78, 3, 25]))
