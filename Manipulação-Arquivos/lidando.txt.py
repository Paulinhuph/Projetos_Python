# =============================================================================
# ETAPA 1: A ESCRITA (PERSISTÊNCIA DOS DADOS)
# Objetivo: Tirar a informação da RAM e "escrever na pedra" (Disco Rígido).
# =============================================================================

# 1. 'with': O Gerenciador de Contexto. Ele abre o arquivo e garante que, 
# ao final do bloco (indentação), o arquivo seja fechado. Isso evita que 
# o arquivo fique "preso" ou corrompido se o programa travar.
#
# 2. 'open()': A função de entrada. 
#    - Parâmetro 1: 'dados.txt' (Nome ou caminho do arquivo).
#    - Parâmetro 2: 'w' (Modo Write/Escrita). 
#      ATENÇÃO: O modo 'w' é destrutivo. Se o arquivo já existir, 
#      ele apaga tudo e começa um novo do zero.
#
# 3. 'as f': Criamos um "apelido" (handle) para o arquivo na memória. 
# Agora, para o Python, 'f' é o nosso arquivo aberto e pronto para ordens.

with open('dados.txt', 'w') as f:
    # O método .write() funciona como a ponta de uma caneta.
    # Ele empurra a string para dentro do arquivo físico.
    f.write('Olá mundo')
    
    # Nota: Ao chegar aqui, o Python encerra o bloco 'with' e FECHA o arquivo.
    # O arquivo 'dados.txt' agora existe fisicamente na sua pasta.

print("--- Sucesso: O arquivo foi criado e os dados foram salvos! ---")


# =============================================================================
# ETAPA 2: A LEITURA (RECUPERAÇÃO DOS DADOS)
# Objetivo: Trazer de volta para o programa o que foi salvo anteriormente.
# =============================================================================

# 1. Aqui usamos o modo 'r' (Read/Leitura). 
# Este modo é "seguro": ele não altera nada, apenas observa o conteúdo.
# Se o arquivo 'dados.txt' não existir, o Python dará um erro (FileNotFoundError).

with open('dados.txt', 'r') as f:
    # MECANISMO: O método .read() percorre o arquivo do início ao fim,
    # copia todo o texto e o entrega para a variável 'conteudo'.
    conteudo = f.read()
    
    # O arquivo é fechado automaticamente aqui.

# 2. EXIBIÇÃO: Agora que o dado está de volta na memória (variável 'conteudo'),
# podemos tratá-lo, filtrá-lo ou apenas exibi-lo.
print("Conteúdo recuperado do arquivo:")
print(conteudo)

# =============================================================================
# 1. MODO APPEND: Adicionando informações sem apagar o passado
# =============================================================================

# INTUIÇÃO: Imagine um diário. Você não apaga as páginas de ontem para escrever 
# as de hoje; você simplesmente vai para a última linha e continua.

with open('dados.txt', 'a', encoding='utf-8') as f:
    # O método .write() aqui não vai sobrescrever o arquivo.
    # Ele vai "pendurar" o texto na última linha existente.
    f.write('\nultima linha') # Usamos \n para garantir que comece em uma nova linha

print("--- Texto acrescentado com sucesso! ---")