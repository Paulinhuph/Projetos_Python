# 💡 Desafio: Calculadora de Bônus Salarial
import time
print('Olá! Sou o Biu, a inteligência artificial da Empresa X. Estou aqui para ajudar você a calcular o bônus salarial dos colaboradores')
time.sleep(1)
print('Ok. Vamos começar!')
print('Digite algumas informações')
time.sleep(1)
print('-----------------------------------------------')

nome = input('Digite o nome do colaborador:')
salario = float(input('Digite o salário atual do colaborador (em R$):'))
nota = float(input('Digite a nota de desempenho do colaborador (de 0 a 10):'))

if nota >= 9:
    bonus = salario * 0.20
    total_c_bonus = salario + bonus
    print('O Funcionário ganhará um bônus de:', bonus, 'Total(R$):', total_c_bonus)
elif  7 <= nota <= 8:
    bonus = salario * 0.10
    total_c_bonus = salario + bonus
    print('O Funcionário ganhará um bônus de:', bonus, 'Total(R$):', total_c_bonus)
elif 5 <= nota <= 6:
    bonus = salario * 0.05
    total_c_bonus = salario + bonus
    print('O Funcionário ganhará um bônus de:', bonus, 'Total(R$):', total_c_bonus)
elif nota < 5:
    bonus = salario * 0
    total_c_bonus = salario + bonus
    print('O Funcionário não ganhará Bônus!')


