#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

"""
import os

yellow = "\033[0;33m"
green = "\033[0;32m"
reset= "\033[m"

def renomear_arquivos(path_pasta: str, prefixo: str):

    contador = 1
    for arquivo in os.listdir(path_pasta):
        if arquivo.endswith(".txt"): # Aqui verifica se é um .txt
            novo_nome = f"{prefixo}{contador}.txt"
            caminho_completo = os.path.join(path_pasta, arquivo)
            novo_caminho_completo = os.path.join(path_pasta, novo_nome)

            os.rename(caminho_completo, novo_caminho_completo) # Renomeia o arquivo atual para o novo nome.
            print(f"Este arquivo {yellow}{arquivo}{reset} foi renomeado para {green}{novo_nome}{reset}")
            contador += 1




if __name__ == "__main__":
    path_pasta = "/home/eddygiusepe/1_Eddy_Giusepe/Exploring_the_World_of_Programming_with_Python/2_Renomeador_de_Arquivos/arquivos_de_teste_em_TXT"
    prefixo = "eddy_name_"
    renomear_arquivos(path_pasta, prefixo)
