biblioteca = {}
def cadastrar_livro(dicionario, nome, livro):
    # Usamos 'dicionario' (o parâmetro), não a variável global
    if nome in dicionario:
        dicionario[nome].append(livro)
    else:
        # Criação da lista inicial para o novo usuário
        dicionario[nome] = [livro]
    # Não precisamos de return, pois dicionários são alterados por referência
    
def obter_livros(dicionario, nome):
    # Verificamos se a chave existe no armário
    if nome in dicionario:
        # Retornamos apenas o conteúdo daquela chave (a lista de livros)
        return dicionario[nome]
    else:
        # Em vez de apenas imprimir, retornamos uma lista vazia para evitar erros futuros
        return []
# --- O MOTOR DE CADASTRO ---
while True: 
    nome = input("Digite o Nome da Pessoa: ")
    livro = input("Digite o Nome do Livro que ela leu: ")
    
    # Chamada CORRETA: Passando a biblioteca e os dados lidos
    cadastrar_livro(biblioteca, nome, livro)
    
    deseja_continuar = input("Deseja Continuar Cadastrando? (s/n): ").lower().strip()
    if deseja_continuar in ["n", "não", "nao"]:
        break
# --- A ETAPA DE CONSULTA (O GRANDE FINAL) ---
print("--- CONSULTA DE LEITURAS ---")
busca = input("De quem você deseja ver a lista de livros? ")

# Aqui usamos a sua SEGUNDA função (obter_livros)
meus_livros = obter_livros(biblioteca, busca)

if meus_livros:
    print(f"Livros lidos por {busca}: {meus_livros}")
else:
    print(f"Nenhum registro encontrado para {busca}.")
