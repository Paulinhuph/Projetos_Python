from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from bson import ObjectId
from app import db  # Seu objeto de conexão com o banco de dados
from app.decorators import token_required  # Seu decorator de proteção

# IMPORTANTE: Você precisa criar e importar estes modelos no seu projeto!
# UserCreate: valida nome, email, senha para o POST
# UserResponse: formata os dados de saída tirando a senha para o GET
from app.models.user import UserCreate, UserResponse 

# Criação do Blueprint dedicado para a rota de usuários
users_bp = Blueprint('users_bp', __name__)


# -------------------------------------------------------------------------
# ROTA 1: GET /usuarios (Listar todos os usuários)
# -------------------------------------------------------------------------
@users_bp.route('/usuarios', methods=['GET'])
@token_required  # Garante que apenas requisições com token válido acessem
def get_all_users(current_user): # Se o seu decorator injeta o usuário, declare-o aqui
    try:
        # Busca todos os registros. O segundo argumento {"password": 0} 
        # diz ao MongoDB para nem trazer a senha do banco, reforçando a segurança.
        users_cursor = db.users.find({}, {"password": 0})
        
        users_list = []
        for user in users_cursor:
            # O MongoDB usa ObjectId. Precisamos converter para string 
            # para que o Pydantic e o JSON consigam serializar corretamente.
            user['_id'] = str(user['_id'])
            
            # Valida e molda os dados usando o modelo de resposta (sem senha)
            validated_user = UserResponse(**user).model_dump(by_alias=True)
            users_list.append(validated_user)
            
        return jsonify(users_list), 200
        
    except Exception as e:
        return jsonify({"error": f"Erro ao listar usuários: {str(e)}"}), 500


# -------------------------------------------------------------------------
# ROTA 2: POST /usuarios (Criar um novo usuário)
# -------------------------------------------------------------------------
@users_bp.route('/usuarios', methods=['POST'])
@token_required
def create_user(current_user):
    try:
        # Captura os dados enviados no corpo da requisição HTTP
        raw_data = request.get_json()
        
        # O Pydantic valida se campos obrigatórios existem e se os tipos estão certos
        user_data = UserCreate(**raw_data)
        
        # Converte o modelo validado em um dicionário Python pronto para o banco
        new_user = user_data.model_dump()
        
        # Opcional: Validar se o email já existe no banco antes de inserir
        if db.users.find_one({"email": new_user["email"]}):
            return jsonify({"error": "Este e-mail já está cadastrado."}), 400
            
        # Insere o dicionário diretamente na collection do MongoDB
        # Nota do desafio: a senha está indo como texto simples conforme permitido
        result = db.users.insert_one(new_user)
        
        # Retorna o ID gerado pelo MongoDB e o status 201 (Created)
        return jsonify({"message": "Usuário criado!", "id": str(result.inserted_id)}), 201
        
    except ValidationError as e:
        # Se os dados enviados não baterem com o UserCreate, exibe os erros estruturados
        return jsonify({"error": "Dados inválidos", "details": e.errors()}), 400
    except Exception as e:
        return jsonify({"error": f"Erro interno ao criar usuário: {str(e)}"}), 500


# -------------------------------------------------------------------------
# ROTA 3: DELETE /usuarios/<id> (Remover usuário por ID)
# -------------------------------------------------------------------------
@users_bp.route('/usuarios/<string:_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, _id):
    try:
        # O MongoDB exige que a busca por ID use a classe ObjectId.
        # Se a string recebida na URL não for um formato válido, o ObjectId lança erro.
        query_id = ObjectId(_id)
        
        # Executa a remoção baseada no ID convertido
        result = db.users.delete_one({"_id": query_id})
        
        # O 'deleted_count' indica quantos documentos foram apagados (0 ou 1)
        if result.deleted_count == 0:
            return jsonify({"error": "Usuário não encontrado."}), 404
            
        # Status 200 com mensagem de sucesso (ou 204 sem corpo)
        return jsonify({"message": "Usuário removido com sucesso!"}), 200
        
    except Exception as e:
        # Captura erros de conversão do ObjectId ou falhas de conexão do banco
        return jsonify({"error": f"Erro ao deletar usuário ou ID inválido: {str(e)}"}), 400