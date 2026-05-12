# -------------------------------------------------
# API - GERENCIADOR DE TAREFAS 
# -------------------------------------------------



# CRUD:
# Um CRUD (Create, Read, Update, Delete) é a espinha dorsal de muitas aplicações web e APIs. 
# Ele permite gerenciar dados de maneira completa: criar, ler, atualizar e excluir. Vamos criar um CRUD simples para gerenciar tarefas.
# Implementando o -- CREATE --
# O CREATE é responsável por adicionar novos registros ao sistema. No Flask, utilizamos o método HTTP POST para isso.
#  Adicione o seguinte código ao seu app.py:
from flask import Flask
from flask import request, jsonify
#(REQUEST: Essencial para interagir com o cliente. 
# Permite usar request.json ou request.get_json() para receber dados enviados em requisições POST ou PUT. 
# Também acessa parâmetros de URL (request.args).)~

# (JSONIFY: jsonify: Essencial para respostas. 
# Transforma listas ou dicionários Python em uma resposta JSON com o tipo MIME correto (application/json), 
# facilitando a leitura por front-ends, como React ou mobile. )

tasks = [] # Lista para armazenar as tarefas
task_id_control = 1 # Trolador de IDs para garantir unicidade

app = Flask(__name__)
from flask_cors import CORS
# ... logo abaixo do app = Flask(__name__)
CORS(app)
# --- CREATE ---
@app.route("/tasks", methods=["POST"]) # Post ---> Envia novos dados pro servidor
def create_task():
    global task_id_control
    data = request.get_json() # Pega os dados enviados no corpo de Requisição
    new_task = {
        "id": task_id_control,
        "title": data.get("title"), # Obtém o título enviado
        "description": data.get("description", ""), # Descrição opcional
        "completed": False # Define que a tarefa começa como incompleta
    }
    tasks.append(new_task) # Adiciona a nova tarefa à lista
    task_id_control += 1 # Incrementa ID para a próxima tarefa 
    return jsonify({"message": "Tarefa criada com sucesso!", "task": new_task}), 201

# Testando o CREATE
# usamos Ferramentas como Postman ou Insomnia:
# 1 - Configure uma requisição POST para o endpoint (rota) /tasks.
# 2 - Envie o seguinte JSON no corpo da requisição:

# Implementando O READ
# Ele permite listar todas as tarefas ou buscar uma tarefa específica pelo ID. 
# Adicione os métodos GET ao app.py

# --- READ (Buscar específica) ---
# Listar TODAS as tarefas
@app.route("/tasks", methods=["GET"]) # Get ---> Recupera os dados já existente
def  get_tasks(): 
    return jsonify({
        "tasks": tasks, "total": len(tasks)
        }), 200

# Buscar uma tarefa ESPECÍFICA
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    # Procura tarefa pelo ID
    task = next((t for t in tasks if t["id"] == task_id), None)
    # Buscamos na nossa lista o dicionário que tem o ID igual ao da URL
    if not task:
        return jsonify({"message": "Tarefa Não encontrada"}), 404
    return jsonify(task), 200
# Testando o READ
# Para listar todas as tarefas, configure uma requisição GET para /tasks.
# Para buscar uma tarefa específica, use GET com /tasks/<ID>. Por exemplo, /tasks/1 retornará:

# Implementando o UPDATE: 
# -- UPDATE --
@app.route("/tasks/<int:task_id>", methods=["PUT"]) # Put ---> Atualiza ou substitui um recurso existente por novos dados
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"message": "Tarefa Não encontrada"}), 404

    # Atualiza os campos da tarefa com os dados enviados
    data = request.get_json()
    task["title"] = data.get("title", task["title"])
    task["description"]= data.get("description", task["description"])
    task["completed"] = data.get("completed", task["completed"])
    return jsonify({"message": "Tarefa Atualizada com sucesso!", "task": task})

# Implementando o Delete
# -- Delete --
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify ({"message": "Tarefa não encontrada"}), 404
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Tarefa deletada com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)