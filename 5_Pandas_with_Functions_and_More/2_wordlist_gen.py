#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Lista de palavras personalizada em Python
=========================================
As listas de palavras podem servir a vários propósitos e podem ser usadas em diferentes contextos,
como criptografia, geração de senhas , quebra de senhas e muito mais. 

Link de estudo --> https://thepythoncode.com/article/make-a-wordlist-generator-in-python
"""
# Importe o módulo argparse para lidar com argumentos de linha de comando.
# Importe o módulo itertools para gerar combinações.
import argparse, itertools

YELLOW = "\033[0;33m"
GREEN = "\033[0;32m"
RESET= "\033[m"
RED = "\033[0;31m"

class WordListGenerator:
    """
    Este script gera uma lista de palavras personalizada semelhante ao crunch.

    Para executar o script, você pode usar os seguintes argumentos de linha de comando:

        -c, --characters: Conjunto de caracteres para incluir na lista de palavras (padrão: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)
        -min, --min_length: Comprimento mínimo das palavras (padrão: 4)
        -max, --max_length: Comprimento máximo das palavras (padrão: 6)
        -out, --output_file: Nome do arquivo de saída (padrão: custom_wordlist.txt)

    Exemplo de uso:
        python 2_wordlist_gen.py -c abc14 -min 3 -max 5 -out generated_passwords.txt
    """
    
    # Defina uma função para gerar uma lista de palavras com base em determinados parâmetros:
    def generate_wordlist(self, characters, min_length, max_length, output_file):
        # Abra o arquivo de saída no modo de gravação:
        with open(output_file, 'w') as file:
            # Itere sobre o intervalo de comprimentos de palavras de min_length a max_length:
            for length in range(min_length, max_length + 1):
                # Gere todas as combinações possíveis de caracteres com o comprimento fornecido:
                for combination in itertools.product(characters, repeat=length):
                    # Junte os caracteres para formar uma palavra e escreva-a no arquivo:
                    word = ''.join(combination)
                    file.write(word + '\n')


    def parse_arguments(self):
        # Crie um objeto ArgumentParser para lidar com argumentos de linha de comando:
        parser = argparse.ArgumentParser(description="Gere uma lista de palavras personalizada semelhante ao crunch.")

        # Definir argumentos de linha de comando:
        parser.add_argument("-c", "--characters", type=str, default="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
                        help="Conjunto de caracteres para incluir na lista de palavras")
        parser.add_argument("-min", "--min_length", type=int, default=4, help="Comprimento mínimo das palavras")
        parser.add_argument("-max", "--max_length", type=int, default=6, help="Comprimento máximo das palavras")
        parser.add_argument("-out", "--output_file", type=str, default="custom_wordlist.txt", help="Nome do arquivo de saída")

        # Analise os argumentos da linha de comando:
        return parser.parse_args()

    def run(self):
        args = self.parse_arguments()

        # Chame a função generate_wordlist com os argumentos fornecidos:
        self.generate_wordlist(args.characters, args.min_length, args.max_length, args.output_file)

        # Imprima uma mensagem indicando que a lista de palavras foi gerada e salva
        print(f"[+] {YELLOW}Lista de palavras gerada e salva em{RESET} {RED}{args.output_file}{RESET}")




if __name__ == "__main__":
    generator = WordListGenerator()
    generator.run()
    