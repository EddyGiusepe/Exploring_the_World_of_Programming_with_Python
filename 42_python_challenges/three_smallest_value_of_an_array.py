#! /usr/bin/env python3
"""
Senior Data Scientist/AI Engineering.: Dr. Eddy Giusepe Chirinos Isidro

-------------------------------------------------
Descrição do Problema: Smallest value of an array
-------------------------------------------------
Escreva uma função que retorne o menor valor de um array
ou o índice desse valor. O 2º parâmetro da função indica
se deve retornar o valor ou o índice.

Suposições:
    - O 1º parâmetro será sempre um array com pelo menos 1 número e sem duplicatas.
    - O 2º parâmetro será uma string com um de dois valores: 'value' ou 'index'.

Exemplos:
    ([1,2,3,4,5], "value")  -->  1
    ([4,0,6,4,2], "index")  -->  1
"""


"""
def smallest_value_of_an_array(array: list, parameter:str) -> int:
    if parameter == "value":
        return min(array)
    elif parameter == "index":
        return array.index(min(array))
"""

def smallest_value_of_an_array(arr: list, t: str) -> int:
    return min(arr) if t=="value" else arr.index(min(arr))



if __name__ == "__main__":
    print(smallest_value_of_an_array([1, 2, 3, 4, 5], "value"))
    print(smallest_value_of_an_array([4, 0, 6, 4, 2], "index"))
    print(smallest_value_of_an_array([1, 2, -2, -5, 0], "index"))
    print(smallest_value_of_an_array([1, 2, -2, -5, 0], "value"))
