#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Usando Hydra para modificar parâmetros ou Hiperparâmetros
=========================================================
Install:
======== $ pip install hydra-core --upgrade

Você pode executar o script, assim:

$ python main.py

ou para modificar parâmetros ou hiperparâmetros, assim:

$ python main.py --batch_size=32     ou      $ python main.py batch_size=32 lr=1e-5
"""
import os
import hydra
from omegaconf import DictConfig

YELLOW = "\033[0;33m"
GREEN = "\033[0;32m"
WHITE = "\033[0;37m"
RED = "\033[0;31m"
RESET= "\033[m"

@hydra.main(version_base="1.3", config_path="./conf", config_name="config")
def func(cfg: DictConfig):
    working_dir = os.getcwd()
    print(f"{GREEN}O diretório de trabalho atual é:{RESET}{YELLOW}{working_dir}{RESET}")

    # To access elements of the config
    print(f"{YELLOW}O tamanho do batch é:{RESET} {cfg.batch_size}")
    print(f"{RED}A learning rate é:{RESET} {cfg['lr']}")





if __name__ == "__main__":
    func()
