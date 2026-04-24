# 💼 Desafio: Sistema de Feedback Inteligente do Colaborador – BiuMind Corp.
import time
from datetime import datetime

data_atual = datetime.now()
print("Data completa:", data_atual)
print('----------------------------------')
time.sleep(1)
print('Olá! Eu sou o Biu, a inteligência Artificial de Sistema de Feedback Inteligente da BiuMind Corp.')
time.sleep(1)
print('O sistema deve avaliar o nível de satisfação interna, a motivação e o comprometimento com projetos de IA.')
time.sleep(1)

# Início
while True:
    nome = input('Digite o Nome do Colaborador:')
    cargo = input('Digite o Cargo do Colaborador:')
    satisfacao = float(input('Digite a nota de Satisfação(0-10):'))
    motivacao = float(input('Digite a nota de Motivação(0-10):'))
    comprometimento = float(input('Digite a nota de Comprometimento(0-10):'))
    time.sleep(1)
    print('Analisando dados...')
    time.sleep(1)

    # Cálculos
    media_colaborador = (satisfacao + motivacao + comprometimento) / 3

    if media_colaborador >= 8:
        print(nome)
        print(cargo)
        print('Excelente engajamento! Candidato ideal para novos projetos de IA.',media_colaborador,'.')
    elif 5 <= media_colaborador <= 7.9:
        print(nome)
        print(cargo)
        print('Bom desempenho, mas com espaço para evolução. Média:',media_colaborador,'.')
    else:
        print(nome)
        print(cargo)
        print('Nível de engajamento baixo. Recomendado acompanhamento do RH. Média:',media_colaborador,'.')
    
    continuar = input('Deseja adicionar outro colaborador? (s/n):').lower()
    if continuar == 'n':
        print('Encerrando Sistema! Obrigado!')
        break

