import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute(
    """
    INSERT INTO estudantes(nome, idade) \
    VALUES(?, ?)
    """,  
    ("Joana", 16)
)
# IMPORTANTE! 
# EspaçoPlaceHolder em consultas preparadas para separar os dados do comando SQL, impedindo que entradas de usuários sejam executadas como código malicioso.
# Ataques a banco de Dados:  a injeção de SQL. A injeção de SQL é um tipo de ataque em que alguém mal-intencionado 
# tenta roubar informações do banco de dados, excluir o banco de dados ou realizar alguma ação prejudicial. Isso é feito inserindo código SQL malicioso em formulários ou durante a manipulação do banco de dados, 
# podendo, por exemplo, excluir todo o banco de dados ou enviar informações para terceiros.

cursor.execute(
    """
        INSERT INTO disciplinas(
            estudante_id, nome_disciplina
        ) VALUES (?, ?)
    """,
    (1, "Matemática")
)
    
conn.commit() # Para confirmar a mudança
conn.close()