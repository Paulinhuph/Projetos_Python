from flask import Blueprint, jsonify, request
from pydantic import ValidationError

category_bp = Blueprint('category_bp', __name__)

# Listar tudo (Read): Uma rota para retornar todas as categorias cadastradas. Geralmente um GET no plural.
@category_bp.route('/categories', methods=['GET'])
def get_categories():
    return jsonify({"message": "Esta é a rota de listagem das categorias"})

# Ver uma específica (Read): Uma rota que recebe um identificador (ID ou Slug) para mostrar detalhes de apenas uma categoria.
@category_bp.route('/categories/<int:category_id>', methods=['GET'])
def get_categories_by_id(category_id):
    return jsonify({"message": f"Esta é a rota de visualização de uma categoria específica conforme seu ID {category_id}"})

# Criar (Create): Uma rota que recebe os dados do seu modelo Category e os salva. Geralmente um POST
@category_bp.route('/categories', methods=['POST'])
def create_categories():
    return jsonify({"message": "Esta é a rota de criação de uma nova categoria"})

# Atualizar (Update): Uma rota para modificar o nome ou a descrição de uma categoria existente. Geralmente um PUT ou PATCH enviando o ID.
@category_bp.route('/categories/<int:category_id>', methods=['PUT'])
def update_categories(category_id):
    return jsonify({"message": f"Esta é a rota de atualização do nome existente com id da categoria {category_id}"})

# Remover (Delete): Uma rota para excluir uma categoria do sistema. Geralmente um DELETE enviando o ID.
@category_bp.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_categories(category_id):
    return jsonify({"message": f"Esta é a rota de deleção de uma categoria."})