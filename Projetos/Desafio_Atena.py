# ⚔️ Desafio: O Julgamento de Atena
import time
print('A Deusa Atena está testando sua sabedoria!')
time.sleep(1)
print('Responda algumas perguntas para que ela julgue se você é digno de entrar no Templo da Sabedoria')
time.sleep(1)
print('---------------------------------------------------------------------------------------------------')

#⚙️ Regras
idade = int(input('Digite sua idade, caro Guerreiro:'))
honra = float(input('Digite quantos pontos de Honra você tem:'))

# Julgamente da Deusa Atena!!
print('A Deusa está analisando seu caso!')
time.sleep(2)
print('TUMMMMMMMMMMM! A Deusa decidiu!')

if idade >= 18 and honra >= 70:
    print("Bem-vindo ao Templo da Sabedoria, guerreiro!")
elif idade < 18 and honra >= 90:
    print("Entrada concedida como aprendiz.")
else:
    print("Acesso negado. Volte quando for digno.")
