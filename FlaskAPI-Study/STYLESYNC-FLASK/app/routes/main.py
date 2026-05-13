from flask import Blueprint, jsonify, request, current_app
from app.models.user import LoginPayload
from pydantic import ValidationError
from app import db
from bson import ObjectId
from app.models.products import * from app.models.sale import Sale
from app.decorators import token_required
from datetime import datetime, timedelta, timezone
import jwt
import csv
import io 

main_bp = Blueprint('main_bp', __name__)

# RF: Autenticação para obter token JWT
@main_bp.route('/login', methods=['POST'])
def login():
    try:
        raw_data = request.get_json()
        user_data = LoginPayload(**raw_data)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except Exception:
        return jsonify({"error": "Erro durante a requisição"}), 500

    if user_data.username == 'admin' and user_data.password == 'supersecret':
        token = jwt.encode(
            { 
                "user_id": user_data.username,
                "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
            },
            current_app.config['SECRET_KEY'],
            algorithm='HS256'
        )
        return jsonify({'access_token': token}), 200

    return jsonify({"message": "Credenciais Inválidas!"}), 401


# RF: Listagem de todos os produtos
@main_bp.route('/products', methods=['GET'])
def get_products():
    products_cursor = db.products.find({})
    products_list = [ProductDBModel(**product).model_dump(by_alias=True, exclude_none=True) for product in products_cursor]
    return jsonify(products_list)

# RF: Criação de um novo produto
@main_bp.route('/products', methods=['POST'])
@token_required
def create_products(token):
    try:
        product = Product(**request.get_json())
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    
    result = db.products.insert_one(product.model_dump())
    return jsonify({"message": "Produto criado com sucesso", "id": str(result.inserted_id)}), 201

# RF: Detalhes de um único produto
@main_bp.route('/product/<string:product_id>', methods=['GET'])
def get_products_by_id(product_id):
    try: 
        oid = ObjectId(product_id)
    except Exception:
        return jsonify({"error": "ID de produto inválido"}), 400
        
    product = db.products.find_one({'_id': oid})
    if product:
        product_model = ProductDBModel(**product).model_dump(by_alias=True, exclude_none=True) 
        return jsonify(product_model)
    return jsonify({"error": "Produto não encontrado!"}), 404

# RF: Atualização de produto existente
@main_bp.route('/products/<string:product_id>', methods=['PUT'])
@token_required
def update_product(token, product_id):
    try:
        oid = ObjectId(product_id)
        update_data = UpdateProduct(**request.get_json())
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    
    update_result = db.products.update_one(
        {"_id": oid},
        {"$set": update_data.model_dump(exclude_unset=True)}
    )

    if update_result.matched_count == 0:
        return jsonify({"error": "Produto não encontrado"}), 404
    
    updated = db.products.find_one({"_id": oid})
    return jsonify(ProductDBModel(**updated).model_dump(by_alias=True))

# RF: Deleção de produto
@main_bp.route('/products/<string:product_id>', methods=['DELETE'])
@token_required
def delete_product(token, product_id):
    try:
        oid = ObjectId(product_id)
    except Exception:
        return jsonify({"error": "ID inválido"}), 400
    
    result = db.products.delete_one({"_id": oid})
    if result.deleted_count == 0:
        return jsonify({"error": "Produto não encontrado!"}), 404
    return "", 204

# RF: Importação de vendas via CSV
@main_bp.route('/sales/upload', methods=['POST'])
@token_required
def upload_sales(token):
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400
    
    file = request.files['file']
    if file.filename == '' or not file.filename.endswith('.csv'):
        return jsonify({"error": "Arquivo inválido"}), 400

    content = file.stream.read().decode('utf-8')
    csv_stream = io.StringIO(content)
    csv_reader = csv.DictReader(csv_stream)

    sales_to_insert = []
    errors = []

    for row_num, row in enumerate(csv_reader, 1):
        try:
            sale_data = Sale(**row)
            sales_to_insert.append(sale_data.model_dump())
        except ValidationError:
            errors.append(f"Linha {row_num}: dados inválidos")
        except Exception:
            errors.append(f"Linha {row_num}: erro inesperado")

    if sales_to_insert:
        db.sales.insert_many(sales_to_insert)

    return jsonify({
        "message": "Processamento concluído",
        "vendas_importadas": len(sales_to_insert),
        "erros_encontrados": errors
    }), 200

@main_bp.route('/')
def index():
    return jsonify({"message": "Bem-vindo ao StyleSync!"})