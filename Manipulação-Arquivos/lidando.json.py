import json # PASSO OBRIGATÓRIO: Importar a biblioteca para tradução de dados

# 1. CONSTRUÇÃO DO OBJETO (Memória RAM)
# Imagine que esses dados vieram de um formulário de cadastro.
dados = {
    'nome': 'Ana',
    'idade': 32,
    'enderecos': ['Endereço A', 'Endereço B'] # Uma lista dentro de um dicionário
}

# =============================================================================
# 2. ESCRITA EM JSON (Serialização)
# =============================================================================

# MECANISMO:
# Usamos o método 'json.dump'. 
# 'Dump' em inglês significa "despejar". Estamos despejando o dicionário no arquivo.

with open('dados.json', 'w', encoding='utf-8') as f:
    # json.dump(objeto_python, arquivo_destino)
    json.dump(dados, f, ensure_ascii=False, indent=4) 
    # DICA EXTRA: 'indent=4' deixa o arquivo bonito/legível para humanos.
    # 'ensure_ascii=False' permite salvar acentos corretamente.

print("--- Arquivo 'dados.json' criado com sucesso! ---")


# =============================================================================
# 3. LEITURA EM JSON (Desserialização)
# =============================================================================

# MECANISMO:
# Usamos o método 'json.load'. Ele "carrega" o texto do arquivo e
# reconstrói automaticamente o dicionário e as listas originais.

with open('dados.json', 'r', encoding='utf-8') as f:
    dados_lidos = json.load(f)

print("\nDados recuperados do JSON:")
print(f"Nome: {dados_lidos['nome']}")
print(f"Primeiro Endereço: {dados_lidos['enderecos'][0]}")