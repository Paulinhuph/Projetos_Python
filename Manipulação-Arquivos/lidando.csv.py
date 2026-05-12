import csv  # PASSO OBRIGATÓRIO: Importar a biblioteca especializada

# =============================================================================
# 2. ESCRITA EM CSV (Criando a "Planilha")
# =============================================================================

# MECANISMO: 
# 1. Abrimos o arquivo normalmente com 'open'.
# 2. Criamos um 'escritor' (csv.writer), que é um tradutor: ele pega listas 
#    do Python e as transforma em linhas separadas por vírgulas.

with open('dados.csv', 'w', newline='', encoding='utf-8') as f:
    # O parâmetro newline='' evita que o Windows pule linhas em branco extras.
    escritor = csv.writer(f)
    
    # row = Linha. O método .writerow() recebe uma LISTA.
    # A primeira linha é o HEADER (Cabeçalho/Nomes das colunas)
    escritor.writerow(['nome', 'idade'])
    
    # As linhas seguintes são os dados propriamente ditos
    escritor.writerow(['Ana', 32])
    escritor.writerow(['Roberto', 27])

print("--- Arquivo CSV 'dados.csv' criado com sucesso! ---")


# =============================================================================
# 3. LEITURA EM CSV (Recuperando a Tabela)
# =============================================================================

# MECANISMO:
# 1. Usamos o 'csv.reader' para interpretar as vírgulas.
# 2. Como o arquivo tem várias linhas, precisamos de um loop 'for' para
#    percorrer o leitor e mostrar uma linha por vez.

print("\nLendo os dados da planilha CSV:")
with open('dados.csv', 'r', newline='', encoding='utf-8') as f:
    leitor = csv.reader(f)
    
    # O leitor entrega cada linha como uma LISTA do Python
    for linha in leitor:
        print(linha) # Ex: ['Ana', '32']