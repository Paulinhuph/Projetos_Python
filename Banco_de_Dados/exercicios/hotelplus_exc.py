# A rede de hotelaria HotelPlus te contratou para criar um pequeno sistema de cadastro de usuários. A priori você precisa criar uma tabela chamada usuarios com os seguintes campos:
# - id (inteiro, chave primária)
# - nome (texto)
# - email (texto)
# Para testar o seu banco de dados, adicione 2 usuários na tabela usuarios e depois consulte todos os registros.

import sqlite3

conn = sqlite3.connect('hotelplus')
cursor = conn.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            idade INTEGER,
            email TEXT NOT NULL
        ) 
""")

cursor.execute (
    """
        INSERT INTO usuarios(
            id, nome, idade, email
        ) VALUES (?, ?, ?, ?)
    """,
    [
        (1, "Carlos Alberto Nascimento", 21, "carlos213hds@email.com")
        (2, "Laisa Moraes Albuquerque", 34, "laisa@email.com")
    ]
)

cursor.execute("SELECT * from usuarios")
for linha in cursor.fetchall():
    print(linha)

conn.commit()
conn.close()