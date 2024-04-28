#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Script de Treinamento
======================
Com este script carregamos o modelo que 
usaremos para treinar nossos dados.

Repare que aqui, também, temos aquela variável: 'config'
a qual é introduzida pelo Hydra.
"""
from sklearn.linear_model import LinearRegression

def train_model(X, y, config):
    model = LinearRegression()
    
    # Treinar o modelo:
    model.fit(X, y)
    
    return model
