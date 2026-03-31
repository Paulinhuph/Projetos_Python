# Avaliação de metas de vendas

nome_vendedor = input('Digite o seu nome:')
valor_total = int(input('Digite o valor total das vendas nesse mês:'))
meta_de_vendas = int(input('Digite a meta de vendas:'))

# O programa deve calcular o percentual de atingimento da meta
print('Olá', nome_vendedor )

# Verificação da meta
percentual = (valor_total / meta_de_vendas) * 100
if percentual < 80:
   print("Meta não atingida.😕")
elif 80 <= percentual < 100:
   print("Quase lá! Continue se esforçando. 💪")
elif percentual >= 100:
   print("Meta atingida! Parabéns! 🏆")
