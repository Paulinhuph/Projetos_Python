# 💻 Desafio: Avaliação de Desempenho dos Colaboradores
# Crie um programa que avalie o desempenho dos colaboradores de uma empresa com base em suas notas de produtividade.
name = input('Digite seu nome, caro colaborador:')
nota = float(input('Digite sua nota de produtividade (0-10):'))

import time 
time.sleep(1)
print('Analisando sua nota...')
print('-----------------------------------------------------')
time.sleep(1)

match nota:
    case 9 | 10:
        print('Bônus de Excelência! Parabéns, colaborador(a)',name + '.', 'Ótimo desempenho!')
    case 7 | 8:
        print('Bônus Padrão! Bom desempenho, colaborador(a)', name + '.', 'Continue assim!')
    case 5 | 6:
        print('Sem Bônus. Colaborador(a)', name + '.', 'Sem Punição, mas é necessário melhorar seu desempenho')
    case nota if nota < 5:
        print('Punição devido baixo desempenho, colaborador(a)', name + '.', 'É necessário melhorar seu desempenho urgentemente!')
        
