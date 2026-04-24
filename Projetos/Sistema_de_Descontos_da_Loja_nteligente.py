# 💼 Desafio: Sistema de Descontos da Loja Inteligente
import time
print('Olá!, sou o Biu, a inteligência Artificial da Loja!')
print('Irei calcular os valores da compra e seus possíveis descontos')
time.sleep(3)
print('Aguarde...')
time.sleep(1)
print('-------------------------------------------------')

nome = input('Digite seu nome:')
valor = float(input('Digite o valor total da compra:'))
cartao = input('Você possui o cartão da loja? (sim/não):').lower()
membro = input('Você é membro do clube de Fidelidade da Loja?(sim/não)').lower()

if cartao == 'sim' and membro == 'sim':
    desconto = valor * 0.20
    valor_total = valor - desconto
    print('Parabéns! Você ganhou um desconto de:', desconto)
    print('O valor da compra foi:', valor, 'Com desconto de 20% ficará:', valor_total)
elif cartao == 'sim' and membro == 'não':
    desconto = valor * 0.10
    valor_total = valor - desconto
    print('Parabéns! Você ganhou um desconto de:', desconto)
    print('O valor da compra foi:', valor, 'Com desconto de 10% ficará:', valor_total)
elif cartao == 'não' and membro == 'sim':
    desconto = valor * 0.05
    valor_total = valor - desconto
    print('Parabéns! Você ganhou um desconto de:', desconto,)
    print('O valor da compra foi:', valor, 'Com desconto de 5% ficará:', valor_total)
elif cartao == 'não' and membro == 'não':
    print('Você não ganhou nenhum desconto. O valor da compra fica em:',  valor)

