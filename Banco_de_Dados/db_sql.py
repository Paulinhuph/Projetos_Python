import sqlite3
# Banco de Dados Relacional

# Conexão:
conn = sqlite3.connect("escola.db")
# Para realizar tarefas:
cursor = conn.cursor()
# Criar uma tabela caso ela não exista
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudantes (
    id INTEGER PRIMARY KEY, 
    nome TEXT,
    idade INTEGER
    )               
""")

cursor.execute(
    "INSERT INTO estudantes (nome, idade)\
    VALUES (?, ?)", ("João", 20))

conn.commit()
# Recuperação e exibição dos dados 
cursor.execute("SELECT * FROM estudantes")
print(cursor.fetchall())
# Fechamento da conexão
conn.close()