#! /usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json

# Inicializar a aplicação Flask
app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas as rotas

# Dados de exemplo para nossa API
tarefas = [
    {"id": 1, "titulo": "Estudar Python", "concluida": False},
    {"id": 2, "titulo": "Testar Thunder Client", "concluida": False},
    {"id": 3, "titulo": "Aprender Flask", "concluida": False}
]

# Rota para a página inicial
@app.route('/', methods=['GET'])
def home():
    return jsonify({"mensagem": "API de Tarefas funcionando!"})

# Rota para obter todas as tarefas
@app.route('/api/tarefas', methods=['GET'])
def get_tarefas():
    return jsonify(tarefas)

# Rota para obter uma tarefa específica pelo ID
@app.route('/api/tarefas/<int:tarefa_id>', methods=['GET'])
def get_tarefa(tarefa_id):
    tarefa = next((t for t in tarefas if t["id"] == tarefa_id), None)
    if tarefa:
        return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

# Rota para adicionar uma nova tarefa
@app.route('/api/tarefas', methods=['POST'])
def add_tarefa():
    if not request.json or not 'titulo' in request.json:
        return jsonify({"erro": "O título da tarefa é obrigatório"}), 400
    
    # Encontrar o próximo ID disponível
    novo_id = max([t["id"] for t in tarefas]) + 1 if tarefas else 1
    
    nova_tarefa = {
        "id": novo_id,
        "titulo": request.json['titulo'],
        "concluida": request.json.get('concluida', False)
    }
    
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

# Rota para atualizar uma tarefa existente
@app.route('/api/tarefas/<int:tarefa_id>', methods=['PUT'])
def update_tarefa(tarefa_id):
    tarefa = next((t for t in tarefas if t["id"] == tarefa_id), None)
    if not tarefa:
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    
    if not request.json:
        return jsonify({"erro": "Dados de atualização não fornecidos"}), 400
    
    tarefa['titulo'] = request.json.get('titulo', tarefa['titulo'])
    tarefa['concluida'] = request.json.get('concluida', tarefa['concluida'])
    
    return jsonify(tarefa)

# Rota para excluir uma tarefa
@app.route('/api/tarefas/<int:tarefa_id>', methods=['DELETE'])
def delete_tarefa(tarefa_id):
    global tarefas
    tarefa = next((t for t in tarefas if t["id"] == tarefa_id), None)
    if not tarefa:
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    
    tarefas = [t for t in tarefas if t["id"] != tarefa_id]
    return jsonify({"mensagem": f"Tarefa {tarefa_id} excluída com sucesso"})

# Executar a aplicação
if __name__ == '__main__':
    app.run(debug=True, port=5000)
