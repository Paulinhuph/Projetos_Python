# 🤖 Desafio: O Despertar da I.A. Oráculo
import time
print('No ano de 3025, você está prestes a ativar a Oráculo, uma I.A. lendária capaz de prever o futuro.')
time.sleep(2)
print('Mas antes que ela desperte, você precisa ajudá-la a despertar!.')
time.sleep(2)
print('Vamos Começar!')
print('____________________________________________________________________________________________________')
# Ínicio
print('Computador - Ajude o Oráculo! Preciso dos seguintes dados:')
time.sleep(2)

energy = float(input('Digite o nível de energia da I.A(0-100):'))
gb = float(input('Digite a quantidade de dados treinados (GB):'))
taxa_precisao = float(input('Digite a taxa de precisão atual (%):'))
time.sleep(1)
print('Carregando...')
time.sleep(1)
print('Computador - Falta Pouco!!!')
time.sleep(1)
print('Quase lá!')
time.sleep(1)
print('AGORA!')
print('...')
time.sleep(1)
# Processo

if energy >= 70 and gb >= 500 and taxa_precisao >= 90:
    print("Oráculo despertou. A singularidade começou! 🤖⚡")
    print('Uma nova era para a humanidade!')
elif energy >= 50 and taxa_precisao >= 70 and gb < 500:
    print("Oráculo ainda está aprendendo... mais dados são necessários. 📚")
else:
    print("Falha no sistema. Oráculo entrou em modo de hibernação. 💤")
