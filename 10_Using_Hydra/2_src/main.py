#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
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
    orig_cwd = hydra.utils.get_original_cwd()
    print(f"{YELLOW}O caminho do 2_src é:{RESET} {orig_cwd}")

    # Read file
    path = f"{orig_cwd}/test.txt"
    with open(path, "r") as f:
        print(f.read())

    # Write file
    path = f"{orig_cwd}/output.txt"
    with open(path, "w") as f:
        f.write("Isto é um cachorro")





if __name__ == "__main__":
    func()
