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

$ python my_app.py db.user=root db.pass=1234     ou      $ python my_app.py db.timeout=30

NOTA: Para poder trocar de DB configura os PATHs aqui --> @hydra.main(version_base="1.3", config_path="./conf/db", config_name="postgresql")
=====
"""
import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base="1.3", config_path="./conf/db", config_name="postgresql")
def my_app(cfg : DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))



if __name__ == "__main__":
    my_app()

