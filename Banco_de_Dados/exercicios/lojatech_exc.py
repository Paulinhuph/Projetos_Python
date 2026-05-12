# A Loja TechMais está informatizando seu controle de estoque
# O gerente quer um sistema simples em Python que registre e consulte produtos no banco de dados loja.db.
# Se conecta ao banco loja.db;
# Crie uma tabela produtos com os campos id, nome, preco;
# Insira 3 produtos diferentes;
# Liste todos os produtos cadastrados.
# Dica: use funções como criar_produto(nome, preco) e listar_produtos().

import sqlite3

def conectar():
    conn = sqlite3.connect('loja.db')
    return conn

def criar_tabelas_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            preco FLOAT NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()

def criar_produto(nome, preco):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
    """
        INSERT INTO produtos (nome, preco)
        VALUES (?, ?)
    """, (nome, preco)
    )
    conn.commit()
    conn.close()

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
            SELECT * FROM produtos
        """
    )

    produtos = cursor.fetchall()
    for produto in produtos:
        print(produto)
        conn.close()

    # --- EXECUÇÃO DO SISTEMA ---
# 1. Preparar o banco
criar_tabelas_produtos()

# 2. Inserir os 3 produtos (como solicitado)
criar_produto("Teclado Mecânico", 250.0)
criar_produto("Mouse Gamer", 120.0)
criar_produto("Monitor 24'", 890.0)

# 3. Mostrar o resultado
print("Produtos no estoque:")
listar_produtos()

# Saída:
# Produtos no estoque:
# (1, 'Teclado Mecânico', 250.0)
# (2, 'Mouse Gamer', 120.0)
# (3, "Monitor 24'", 890.0)