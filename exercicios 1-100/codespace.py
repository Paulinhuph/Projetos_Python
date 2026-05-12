def gerar_tabuada(numero_digitado):
    # Gera e exibe no console as tabuadas de multiplicação do 0 até o número fornecido.
    #   numero_digitado (int): O limite superior de qual tabuada será calculada.
    # Loop externo: define qual tabuada está sendo calculada no momento (de 0 até o limite)
    for i in range(0, numero_digitado + 1):
        print(f"\n---Tabuada do {i}---")
        
        # Variável auxiliar (calcula o produto do limite pelo índice atual)
        tabuada = numero_digitado * i
        
        # Loop interno: percorre os multiplicadores de 0 a 10 para a tabuada atual (i)
        for j in range(0, 11):
            resultado = i * j
            # Exibe a linha da tabuada formatada
            print(f"{i} x {j} = {resultado}")
# Entrada de dados: solicita ao usuário um número inteiro
numero_digitado = int(input("Digite o Número para exibição das Tabuadas: "))
# Chamada da função passando o valor digitado pelo usuário
tabuadas = gerar_tabuada(numero_digitado)