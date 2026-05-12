import sqlite3

conn = sqlite3.connect('escola.db') # Cria a conexão
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS estudantes(
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        idade INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS disciplinas(
        id INTEGER PRIMARY KEY,
        nome_disciplina TEXT NOT NULL,
        estudante_id INTEGER,
        FOREIGN KEY (estudante_id) REFERENCES estudantes(id)
    )
''')

conn.commit()
conn.close() # Fecha a Conexão com o Banco de Dados 