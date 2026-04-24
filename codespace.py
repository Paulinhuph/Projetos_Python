soma_todos_valores = 0
menor_valor_digitado = []
quantidade_valores_digitados = 0
valores_pares = 0

while True: 
    numero = float(input("Digite o número: "))
    menor_valor_digitado.append(numero)
    quantidade_valores_digitados += 1
    soma_todos_valores += numero

    if numero % 2 == 0:
        valores_pares += 1

    deseja_continuar = input("Deseja Adicionar mais números? (sim/não): ").strip().lower()
    if deseja_continuar in ['n', 'não', 'nao']:
        break

if quantidade_valores_digitados > 0:
    media = soma_todos_valores / quantidade_valores_digitados
else:
    media = 0

print("-" * 30)
print(f"a) Quantas idades foram registradas: {quantidade_valores_digitados} valores.")
print(f"b) O Menor valor digitado foi: {min(menor_valor_digitado)}")  
print(f"A Média entre os valores foi: {media:.1f}")
print(f"O Total de Valores pares foi: {valores_pares} números pares.")      