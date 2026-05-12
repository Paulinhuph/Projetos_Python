from pymongo import MongoClient
# Banco de Dados Não-Relacional, NoSQL

client = MongoClient("mongodb://localhost:27017/")
db = client["escola"]
estudantes = db["estudantes"]
# Inserindo:
# Apagar o nome e idade, salvar e automáticamente salva 
estudantes.insert_one({"nome": "Lucas", "idade": 22})
# Exibição:
for estudante in estudantes.find():
    print(estudante)