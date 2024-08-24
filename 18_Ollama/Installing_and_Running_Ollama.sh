#!/bin/bash

# Baixa e executa o script de instalação do Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Inicia o servidor Ollama
ollama serve

# Lembrar a execução ---> ./Installing_and_Running_Ollama.sh
# Dar permissão --> chmod +x Installing_and_Running_Ollama.sh
# ollama pull phi3:3.8b
# ollama pull llama2:7b
# ollama list
# ollama run llama3.1:8b