#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Usanndo logging dentro do Hydra
===============================
Você pode executar o script assim:
$ python main.py

ou, assim (para mostrar o debug):

$ python main.py hydra.verbose=true
"""
import hydra
from omegaconf import DictConfig

YELLOW = "\033[0;33m"
GREEN = "\033[0;32m"
WHITE = "\033[0;37m"
RED = "\033[0;31m"
RESET= "\033[m"


import logging
log = logging.getLogger(__name__)

@hydra.main(version_base="1.3", config_path="./conf", config_name="config")
def main_func(cfg: DictConfig):
    log.debug("Debug level message")
    log.info("Info level message")
    log.warning("Warning level message")



if __name__ == "__main__":
    main_func()
