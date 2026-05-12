import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute(
    """
        SELECT * FROM estudantes
    """
)

cursor.execute(
    """
        SELECT * FROM disciplinas
    """
)
estudantes = cursor.fetchall()
for estudante in estudantes:
    print(estudante)

disciplinas = cursor.fetchall()
for disciplina in disciplinas:
    print(disciplina)

conn.commit()
conn.close()

# Exemplos de Consultas e boas Práticas:
# No terminal:
# cursor.execute("""SELECT estudantes.nome, disciplinas.nome_disciplinas FROM disciplinas JOIN estudantes ON disciplinas.""")
# Retorna um objeto
# print(cursor.fetchall()) para ler o Objeto retornado

# Use sempre ? para passar parâmetros evitando a Injeção de BD
# Use IF NOT EXISTS ao criar tabelas
# Use conn.commit()
# Use conn.close()
