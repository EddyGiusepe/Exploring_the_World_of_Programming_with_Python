#! /usr/bin/env python3
"""
Senior Data Scientist/AI Engineering.: Dr. Eddy Giusepe Chirinos Isidro

---------------------------------------
Descrição do Problema: Largest Elements
---------------------------------------
Complete a função que recebe uma lista de números
e um número n, e retorne os n maiores elementos da
lista.

n = 2; list = [7, 6, 5, 4, 3, 2, 1]
==> [6, 7]
n = 3; list = [4, 9, 3, 4, 5, 1, 8]
==> [9, 8, 5]
"""

"""
def largest_elements(lista: list[int], n: int) -> list[int]:
    return sorted(lista)[-n:]


if __name__ == "__main__":
    print(largest_elements([4, 2, 3, 4, 5, 8, 8], 3))
"""


# Aqui vou resolver o problema usando CLASS em Python:
class Ranking:
    def __init__(self, lista: list[int]) -> None:
        self.lista = lista

    def the_n_largest_numbers(self, n: int) -> list[int]:
        print(f"A minha lista em forma crescente: {sorted(self.lista)}")
        return sorted(self.lista)[-n:]


if __name__ == "__main__":
    ranking = Ranking([4, 2, 3, 4, 5, 8, 8])
    print(ranking.the_n_largest_numbers(3))
