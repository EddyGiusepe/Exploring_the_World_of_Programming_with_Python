#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Usando Hydra para nosso projeto de ML
=====================================
Aqui executamos ese script principal (main.py)
a qual é um pipeline de todo o fluxo de nosso projeto
de ML. 

Execução:
=========
$ python main.py
"""
import hydra
from omegaconf import DictConfig
from sklearn.model_selection import train_test_split
from data import load_data
from train import train_model
from evaluate import evaluate_model

YELLOW = "\033[0;33m"
GREEN = "\033[0;32m"
WHITE = "\033[0;37m"
RED = "\033[0;31m"
RESET= "\033[m"


@hydra.main(version_base="1.3", config_path=".", config_name="config")
def main(config: DictConfig):
    # Carregar os dados:
    X, y = load_data(config)
    
    # Dividir os dados em conjuntos de treinamento e teste:
    # (Nota: esta parte pode ser feita aqui ou na função load_data)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)
    
    # Treinar o modelo:
    model = train_model(X_train, y_train, config)
    
    # Avaliar o modelo:
    mse = evaluate_model(model, X_test, y_test)
    
    print(f"{YELLOW}O Erro Quadrático Médio (MSE) é:{RESET} {mse}")




if __name__ == "__main__":
    main()
