# 💡 Desafio: Sistema de Acesso ao Escritório
print('Olá! Sou o Biu, Agente artificial da Empresa.')
print('Para entrar no escritório, preciso que você me passe algumas informações.')
import time
time.sleep(1)
print('_____________________________________________________________________')
time.sleep(1)

nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))
tem_cracha = input('Você possui um crachá de acesso? (sim/não):').lower().strip()
time.sleep(1)
print('___________________________________________________________________')

if idade >= 18 and tem_cracha == 'sim':
    print('Maior de idade e com crachá confirmado.')
    print('Acesso Liberado! Bem-Vindo ao Escritório do HMJJM!')
elif idade < 18 and tem_cracha == 'sim':
    print('Menor de idade, mas com crachá confirmado.')
    print('Acesso Negado! Local Proibido a menores!')
elif idade >= 18 and tem_cracha == 'não':
    print('Maior de idade, mas sem crachá.')
    print('Acesso Negado! Você precisa de um crachá para entrar.')
else:
    print('Menor de idade e sem crachá.')
    print('Acesso Negado! Local Proibido a menores e sem crachá.')
