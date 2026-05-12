import sqlite3
# Função para conexão com o Banco de Dados
def conectar():
    conn = sqlite3.connect('escola.db')
    return conn

def criar_tabela_estudantes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS estudantes(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            idade INTEGER
        )
    """
    )
    conn.commit()
    conn.close()

def criar_tabela_matricula():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS matriculas(
                id INTEGER PRIMARY KEY,
                nome_disciplina TEXT,
                estudante_id INTEGER,
                FOREIGN KEY (estudante_id) REFERENCES estudante(id)
            )
        """
    )
    conn.commit()
    conn.close()

def criar_estudante(nome, idade):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
            INSERT INTO estudantes (nome, idade),
            VALUES (?, ?)
        """, (nome, idade)
    )
    conn.commit()
    conn.close()

def listar_estudantes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
            SELECT * FROM estudantes
        """
    )
    estudantes = cursor.fetchall()
    for estudante in estudantes:
        print(estudante)
    conn.commit()
    conn.close()

def criar_matricula(estudante_id, nome_disciplina):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
    """
        INSERT INTO matriculas (estudante_id, nome_disciplina),
        VALUES (?, ?)
    """, (estudante_id, nome_disciplina)
    )
    conn.commit()
    conn.close()

def listar_matriculas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
            SELECT matriculas.id, estudantes.nome, matriculas.nome_disciplina
            FROM matriculas
            JOIN estudantes ON matriculas.estudante_id = estudantes.id
        """
    )
    # JOIN: Para buscar o relacionamento entre a tabela de matrículas e a de estudantes
    matriculas = cursor.fetchall()
    for matricula in matriculas:
        print(matricula)
    conn.commit()
    conn.close()

    # Para executar, no terminal: 
    # python
    # >>> exec9open('db.py').read())
    # >>> criar_matricula(1, "matemática")
    # >>> listar_matricula()

    # APIREST: Uma API REST é uma Application Programming Interface (Interface de Programação de Aplicações), 
    # que permite a comunicação entre sistemas. 
    # O REST, por sua vez, significa Representational State Transfer (Transferência de Estado Representacional). Trata-se de uma arquitetura, uma padronização de como transferimos dados entre sistemas.
    #  A API REST utiliza métodos HTTP.

    