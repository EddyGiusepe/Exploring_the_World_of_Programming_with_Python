#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Upload de nossos Dados
======================
Este script sube nossos dados. 
Perceba que ele recebe uma variável do tipo
'config', a qual tem uma estrutura de dado do tipo
dicionário.
"""
import pandas as pd

def load_data(config):
    dataset = config.data.dataset
    target_column = config.data.target_column
    feature_columns = config.data.feature_columns
    
    # Carregar o conjunto de dados
    data = pd.read_csv(dataset)
    
    # Selecionar apenas as colunas de características e o alvo
    data = data[[target_column] + feature_columns]

    # Codificar variáveis categóricas (se necessário)
    data = pd.get_dummies(data, columns=['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea', 'furnishingstatus'], drop_first=True)

    # Dividir os recursos (X) e o alvo (y)
    X = data.drop(columns=[target_column])
    y = data[target_column]
    
    return X, y
