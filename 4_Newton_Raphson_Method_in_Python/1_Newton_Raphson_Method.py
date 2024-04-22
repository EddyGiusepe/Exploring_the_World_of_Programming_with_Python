#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

NOTA:
Não executar porque demora muito!
"""

import numpy as np
from tqdm import tqdm

# Exemplo básico para a seguinte função:
def f(x):
    return x**2 + 2

# Definimos a sua derivada:
def f_prime(x):
    return 2*x


def my_newton(f, df, x0, tol):
    """
    Encontra a raiz de uma função usando o método Newton-Raphson.

    Args:
        f: Objeto de função representando f(x)
        df: Objeto de função representando f'(x)
        x0: Suposição inicial
        tol: Tolerância a erros

    Returns:
            Raiz estimada
    """
    # Verifique se a estimativa inicial já está próxima da raiz:
    if abs(f(x0)) < tol:
        return x0
    else:
        with tqdm() as pbar:
            # Atualize a estimativa iterativamente até a convergência:
            while True:
                x1 = x0 - f(x0) / df(x0) # x_new = x_old - function(x_old) / function_derivative(x_old)
                if abs(x1-x0) < tol:
                    pbar.close()
                    return x1
                x0 = x1
                pbar.update()


if __name__ == '__main__':
    initial_guess = 1.4
    tolerance = 1e-1 # Defina a tolerância desejada

    estimated_root = my_newton(f, f_prime, initial_guess, tolerance)

    print(f"Raiz estimada usando o método Newton-Raphson, é: {estimated_root}")
    
    print("Atual valor de √2: ", np.sqrt(2))

