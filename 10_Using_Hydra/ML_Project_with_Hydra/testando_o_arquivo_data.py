#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Upload de nossos Dados
======================
Com este script vou testar o script (data.py) que sube
nosso dados. Perceba que o 'config' tem uma estructura
do tipo dicionário.
"""
import pandas as pd
import data  # Importa o módulo data.py que contém a função load_data()
from omegaconf import OmegaConf

YELLOW = "\033[0;33m"
GREEN = "\033[0;32m"
WHITE = "\033[0;37m"
RED = "\033[0;31m"
RESET= "\033[m"

# Função de teste para a função load_data()
def test_load_data():
    # Dados de teste
    config = OmegaConf.create({
        "data": {
            "dataset": "./Housing.csv",
            "target_column": "price",
            "feature_columns": ['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea', 'furnishingstatus']
        }
    })
    
    # Chama a função load_data() com os dados de teste
    X, y = data.load_data(config)
    x_df = pd.DataFrame(X)
    print(f"As colunas de X, são: {YELLOW}{x_df.columns}{RESET}")
    print(x_df.shape)
    print("")
    y_df = pd.DataFrame(y)
    print(f"A coluna de y, é: {RED}{y_df.columns}{RESET}")
    print(y_df.shape)

    # Adicione mais verificações conforme necessário
    
    print(f"{GREEN}Teste para carregar nossos Dados passou com sucesso!{RESET}")

if __name__ == "__main__":
    # Chama a função de teste
    test_load_data()
