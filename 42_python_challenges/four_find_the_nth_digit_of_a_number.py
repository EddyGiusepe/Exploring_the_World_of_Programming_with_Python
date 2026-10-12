#! /usr/bin/env python3
"""
Senior Data Scientist/AI Engineering.: Dr. Eddy Giusepe Chirinos Isidro

-----------------------------------------------------
Descrição do Problema: Find the nth Digit of a Number
-----------------------------------------------------
Complete a função que recebe dois números como entrada, num e nth,
e retorne o nth dígito de num (contando da direita para a esquerda).

Observações:
    - Se num for negativo, ignore o sinal e trate-o como positivo.
    - Se nth não for positivo, retorne -1.
    - Lembre-se que 42 = 00042, portanto find_digit(42, 5) retornaria 0.

Exemplos:
    (num, nth --> saída):
    5673,  4  -->  5
    129,   2  -->  2
    -2825, 3  -->  8
    -456,  4  -->  0
    0,     20 -->  0
"""


def find_digit(num: int, nth: int) -> int:
    if nth <= 0:
        return -1
    return abs(num) // 10 ** (nth - 1) % 10


if __name__ == "__main__":
    print(find_digit(5673, 2))
    print(find_digit(5673, 5))
    print(find_digit(-2825, 3))
    print(find_digit(-456, 4))
    print(find_digit(0, -20))
