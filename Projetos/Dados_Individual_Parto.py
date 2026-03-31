# 👶 Exercício de Lógica de Programação — Registro Individual de Parto
# Descrição do problema: O hospital JJMS Maternidade Estadual quer registrar os dados de um único parto para gerar um relatório automático.
# O programa deve receber as informações da paciente, do médico e do bebê, e no final exibir um pequeno resumo colorido e formatado.

import time
from datetime import datetime
agora = datetime.now()
print(agora.strftime("%d/%m/%Y %H:%M"))

# Inserir dados Puérpera:
print('\033[1;34;40mOlá Colaborador!\033[m')
time.sleep(1)
print('O sistema vai registrar as informações do Parto e emitir um relatório.')
nome = input('Digite o Nome completo da Paciente: ')
idade = int(input('Digite a idade da Paciente: '))
tipo_parto = input('Digite o Tipo de via de Parto(Normal/Cesariana): ').lower()
indicacao = input('Digite a indicação do Parto: ')
idade_gestacional = float(input('Digite a Idade Gestacional: '))
medico_go = input('Digite o Nome do Médico Obstétra que realizou o Parto: ')
time.sleep(1)

# Dados do Recém-nascido:
print('Agora informe os dados do RN.')
time.sleep(1)
rn_data_nasc = input('Digite a Data do Nascimento: ')
rn_hora = input('Digite a hora do nascimento: ')
peso = float(input('Digite o Peso (KG): '))
aspirado = input('O RN foi aspirado? (sim/não): ').lower()
reanimado = input('O RN foi reanimado? (sim/não):  ').lower()
time.sleep(1)
print('-' * 60)
time.sleep(2)

# Análise:
agora = datetime.now()
print(agora.strftime("%d/%m/%Y %H:%M"))
print('Analisando dados...')
time.sleep(1)
print('-' * 5, '\033[1;34;40mRelátorio do Parto.\033[m', '-' * 5)
print('Parturiente.')
time.sleep(1)
print('Nome: {}.'.format(nome))
time.sleep(1)
print('idade: {}.'.format(idade))
if idade < 18:
    print('Puérpera menor de idade.')
elif idade < 30 and tipo_parto == 'Normal':
    print('Parturiente de Baixo Risco.')
time.sleep(1)
if idade_gestacional < 36:
    print('Prematuro: {} semanas.'.format(idade_gestacional))
else:
    print('Termo.')
    time.sleep(1)
    print('Idade Gestacional: {}.'.format(idade_gestacional))
time.sleep(1)
print('Indicação: {}.'.format(indicacao))
time.sleep(1)
print('Via de Parto: {}.'.format(tipo_parto))
time.sleep(1)
print('Médico G.O e Obstétra: {}.'.format(medico_go))
time.sleep(2)
print(' ')

# RN
print('Recém-Nascido.')
time.sleep(1)
print('Data Nascimento: {}'.format(rn_data_nasc))
time.sleep(1)
print('Hora Nascimento: {}'.format(rn_hora))
if peso < 2100:
    print('Baixo Peso, RN encaminhado para UTI Neo, {} KG'.format(peso))
else:
    print('Peso: {}'.format(peso))
time.sleep(1)
print('Aspirado: {}'.format(aspirado))
time.sleep(1)
print('Reanimado: {}'.format(reanimado))
print('\n' + '-' * 60)
print('\033[1;32mRelatório Final Gerado com Sucesso!\033[m')
print('-' * 60)



