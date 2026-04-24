# 👶 Exercício de Lógica de Programação — Controle de Partos em uma Maternidade
# A maternidade deseja um sistema simples que receba e processe os dados dos partos realizados no ano
# O programa deve permitir ao usuário registrar os partos, guardando tipo de parto.
# Realizar a contagem total de parto do ano, sua média e se é superior ou inferior ao ano anterior
import time
print('Olá Colaborador!')
print('O sistema irá carregar...')
time.sleep(1)
print('Aguarde!')
time.sleep(1)
print('Tudo Pronto!')
print('JJMS Maternidade Estadual')
print('_' * 35)
total_partos1 = []
total_cesariana = []
total_normal = []

quantidade_partos1 = int(input('Digite o número de partos do mês (Janeiro): '))
quantidade_partos2 = int(input('Digite o número de partos do mês (Fevereiro): '))
quantidade_partos3 = int(input('Digite o número de partos do mês (Março): '))
quantidade_partos4 = int(input('Digite o número de partos do mês (Abril): '))
quantidade_partos5 = int(input('Digite o número de partos do mês (Maio): '))
quantidade_partos6 = int(input('Digite o número de partos do mês (Junho): '))
quantidade_partos7 = int(input('Digite o número de partos do mês (Julho): '))
quantidade_partos8 = int(input('Digite o número de partos do mês (Agosto): '))
quantidade_partos9 = int(input('Digite o número de partos do mês (Setembro): '))
quantidade_partos10 = int(input('Digite o número de partos do mês (Outubro): '))
quantidade_partos11 = int(input('Digite o número de partos do mês (Novembro): '))
quantidade_partos12 = int(input('Digite o número de partos do mês (Dezembro): '))
time.sleep(1)

total_partos1 = (quantidade_partos1 + quantidade_partos2 + quantidade_partos3 + quantidade_partos4 + quantidade_partos5 + quantidade_partos6 + quantidade_partos7 + quantidade_partos8 + quantidade_partos9 + quantidade_partos10 + quantidade_partos11 + quantidade_partos12)

print('O total foram de: {}.'.format(total_partos1))
time.sleep(1)
tipon = int(input('Digite quantos foram parto normal do total anual: '))
tipoc = int(input('Digite quantos foram parto Cesariana do total anual: '))

total_cesariana.append(tipoc)
total_normal.append(tipon)

# Cálculo da Média de Partos
media = total_partos1 / 12

# O sistema deve mostrar:
print("\nRelatório Mensal de Partos")
time.sleep(1)
print('-' * 70)
time.sleep(1)
print('O total de Partos do Ano foram: {}.'.format(total_partos1))
print('Aqui está os números de cada mês:')
time.sleep(1)
print('Janeiro: {} Partos.'.format(quantidade_partos1))
time.sleep(1)
print('Fevereiro: {} Partos.'.format(quantidade_partos2))
time.sleep(1)
print('Março: {} Partos.'.format(quantidade_partos3))
time.sleep(1)
print('Abril: {} Partos.'.format(quantidade_partos4))
time.sleep(1)
print('Maio: {} Partos.'.format(quantidade_partos5))
time.sleep(1)
print('Junho: {} Partos.'.format(quantidade_partos6))
time.sleep(1)
print('Julho: {} Partos.'.format(quantidade_partos7))
time.sleep(1)
print('Agosto: {} Partos.'.format(quantidade_partos8))
time.sleep(1)
print('Setembro: {} Partos.'.format(quantidade_partos9))
time.sleep(1)
print('Outubro: {} Partos.'.format(quantidade_partos10))
time.sleep(1)
print('Novembro: {} Partos.'.format(quantidade_partos11))
time.sleep(1)
print('Dezembro: {} Partos.'.format(quantidade_partos12))
time.sleep(1)
print('A média de Partos foram: {} Partos.'.format(media))
ano_anterior = int(input('Digite o número total do ano anterior: '))
if total_partos1 < ano_anterior:
    print('O número de Partos totais foram inferiores ao total do ano anterior.')
elif total_partos1 > ano_anterior:
    print('O número de Partos totais foram superiores ao total do ano anterior.')
else: 
       print('O número de Partos totais foram iguais ao total do ano anterior.')


