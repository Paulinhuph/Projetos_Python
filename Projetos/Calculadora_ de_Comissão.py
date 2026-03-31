# calculadora de vendas e comissão
print('💼 Calculadora de Vendas e Comissão')
print('-' * 35)


vendas = int(input("Quantos produtos foram vendidos no mês?"))
produto = float(input("Qual valor de cada produto?"))

total = vendas * produto
comissão = total * 0.05
print("Total vendido foi:", total)
print("A comissão de 5% foi de:", comissão)
total_recebido = 1500 + comissão
print("O total recebido foi de 1500 + comissão:", total_recebido)
