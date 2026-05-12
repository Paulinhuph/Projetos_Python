# exF01 (Hello JSON): Crie uma rota GET em /api que retorne um objeto JSON com a chave "mensagem" e o valor "API Ativa".
from flask import Flask
from flask import request, jsonify

app = Flask(__name__)
@app.route("/api", methods=["GET"])
def hellojson():
    return jsonify({"mensagem": "API Ativa"}), 200 # <-- Aqui está o que você Pediu! 

if __name__ == "__main__":
        app.run(debug=True)
# ------------------------------------------------------------------------------------------------

# exF02 (Saudação Dinâmica): Desenvolva um endpoint que receba um nome via âparmetro de rota (/saudar/<nome>) e retorne uma saudação personalizada.
from flask import Flask
from flask import request, jsonify

app = Flask(__name__)
@app.route("/saudar/<nome>", methods=["GET"])
def retornarmensagem(nome):
      return jsonify({"mensagem": f"Olá, {nome}"})  
    
if __name__ == "__main__":
        app.run(debug=True)
# ---- Comentários ---- 
# A Captura: Quando você escreve @app.route("/saudar/<nome>"), os símbolos < > dizem ao Flask: 
# "O que vier depois de /saudar/ não é texto fixo, é um dado dinâmico. 
# Capture-o e chame-o de 'nome'".

# retornarmensagem(nome) aceita um argumento com o 
# mesmo nome que ele acabou de capturar na URL.

# ----------------------------------------------------------------------------------------------------

# exF03 (Calculadora POST): Crie uma rota POST que receba dois números em um JSON e retorne a soma deles.

from flask import Flask
from flask import request, jsonify

app = Flask(__name__)
@app.route("/soma", methods=["POST"])
def calculadora():
    dados = request.get_json()
    n1 = dados.get('num1')
    n2 = dados.get('num2')
    resultado = n1 + n2
    return jsonify({"resultado": f" A soma entre {n1} e {n2} é {resultado}"})

if __name__ == "__main__":
        app.run(debug=True)
# ----------------------------------------------------------------------------------------------------


# exF04 (Conversor de Moeda): Implemente um endpoint que receba um valor em Reais via Query String (?valor=10) e retorne o equivalente em Dólares (considere US$1 = R$6).

from flask import Flask
from flask import request, jsonify
# A rota é apenas o endereço do recurso. 
app = Flask(__name__)
@app.route("/conversor", methods=["GET"])
def conversor():
    # Captura o valor da URL. Ex: /conversor?reais=60
    valor_reais = request.args.get('reais') # Query strings ficam na URL e são acessadas via request.args
    dolar = float(valor_reais) / 6
    return jsonify({
          "reais": valor_reais,
          "dolares": round(dolar, 2)
    })

if __name__ == "__main__":
        app.run(debug=True)
    
# ----------------------------------------------------------------------------------------------------

# exF05 (Validador de Acesso): Construa uma rota que verifique um "Token" enviado no cabeçalho (Header) da requisição; retorne erro 401 se estiver incorreto.

from flask import Flask
from flask import request, jsonify

app = Flask(__name__)
@app.route("/verificador", methods=["GET"])
def verificacao():
      token_correto = "MINHA_CHAVE_123"
      token_recebido = request.headers.get('Token')
      if token_recebido == token_correto:
            return jsonify({"mensagem": "Acesso liberado"}), 200 # Sucesso
      return jsonify({"erro": "Não Autorizado!"}), 401


if __name__ == "__main__":
        app.run(debug=True)

# ----------------------------------------------------------------------------------------------------
# exF06 (Dicionário de Dados): Simule um banco de dados com uma lista de dicionários de usuários e crie uma rota GET que liste todos.
from flask import Flask
from flask import request, jsonify

app = Flask(__name__)
# Uma única lista com vários dicionários
db =   [
      {
        "id": 1,
      "email": "phasikF@gmail.com",
      "nome": "Luan da Costa"
        },
        {
        "id": 2,
      "email": "phasgfvF@gmail.com",
      "nome": "Pedro Sampaio"
        }
]
@app.route("/usuario", methods=["GET"])
def dados_usuarios():
        # Retorna a lista inteira diretamente
        return jsonify(db), 200

if __name__ == "__main__":
        app.run(debug=True)

# -----------------------------------------------------------------------------
# exF07 (Busca por ID): Crie um endpoint que busque um usuário específico pelo ID informado na URL; retorne erro 404 caso o ID não exista na lista.
from flask import Flask
from flask import request, jsonify
app = Flask(__name__)

lista_id = [1, 2, 4]
# Garante que o usuário digite um número inteiro (conversor <int:id>)
@app.route("/usuario/<int:id>", methods=["GET"])
def buscausuario(id):
        if id in lista_id:
               return jsonify({"message": "ID Encontrado!"}), 200
        return jsonify({"message": f"Erro! ID não encontrado."}), 404

if __name__ == "__main__":
        app.run(debug=True)

# -----------------------------------------------------------------------------
# exF08 (Filtro de Preço): Desenvolva uma rota para produtos que aceite parâmetros de Query para filtrar itens acima de um valor mínimo enviado pelo usuário.

from flask import Flask
from flask import request, jsonify
app = Flask(__name__)

@app.route("/preco", methods=["GET"])
def buscar_preco():
        # O .get aceita um segundo argumento: o valor padrão (default)
        # IMPORTANTE: request.args sempre traz strings. 
        # Usamos type=int para o Flask converter para nós.
        preco_minimo = request.args.get('minimo', default=0, type=int)
        return jsonify ({"resultado": f"Filtro produtos acima de: R$ {preco_minimo} reais"}), 200

if __name__ == "__main__":
        app.run(debug=True)

# -----------------------------------------------------------------------------
# exF09 (Atualizador de Status): Implemente um método PUT que receba o ID de uma tarefa e altere seu status de "pendente" para "concluído" na sua lista em memória.
from flask import Flask
from flask import request, jsonify
task = [
       {
                "tarefa": "Aprender Python",
                "status": "Incompleta",
                "task_id": 1
       }
        ]
app = Flask(__name__)

app.route("/tasks/<int:task_id>", methods=["PUT"])
def atualizartarefa(task_id):
       item = next((t for t in task if t["task_id"] == task_id), None)
       if item is None:
            return jsonify({"erro": "Tarefa não encontrada"}), 404
       item["status"] = "concluído"
       return jsonify({
              "message": "Status atualizado com sucesso!",
              "tarefa": item
       }), 200

if __name__ == "__main__":
       app.run(debug=True)

# -----------------------------------------------------------------------------
# exF10 (Deleção Segura): Crie um endpoint DELETE que remova um registro da lista baseando-se no ID e retorne uma mensagem confirmando a exclusão.
from flask import Flask
from flask import request, jsonify
app = Flask(__name__)

registros = [
       {"id": 1, "registro": "Alteração Email"}
]
@app.route("/excluir/<int:id>", methods=["DELETE"])
def delete(id):
        global registros # Necessário para modificar a variável global
        # Localização
        item = next((r for r in registros if r['id'] == id), None)
        if item is None:
                return jsonify({'erro': "Registro não encontrado!"}), 404
    # Deleção (Filtrando a lista para remover o ID)
        registros.remove(item)
        return jsonify({'status': 'removido!'}), 200

if __name__ == "__main__":
       app.run(debug=True)

       