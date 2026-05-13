from flask import Flask
from .routes.main import main_bp
from .routes.user_routes import users_bp
from .routes.category_routes import category_bp
from pymongo import MongoClient

db = None
def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    app.register_blueprint(category_bp, url_prefix='/categories')
    app.register_blueprint(users_bp, url_prefix='/users')
    app.config.from_object('config.Config')
    global db

    try:
        client = MongoClient(app.config['MONGO_URI'])
        db = client.get_default_database()
    except Exception as e:
        print('Erro ao realizar a conexão com o banco de dados: {e}')

    from .routes.main import main_bp

    return app