# Desafio: Painel de Desempenho da Empresa
colaboradores = ['Paulo', 'Lucas', 'Daniel', 'Felipe', 'Samuel', 'Ricardo']
notas = []
import time
while True:
    nome = input('Digite o nome do colaborador:') 
    nota = int(input('Digite a nota do colaborador (de 0 a 10):'))

    colaboradores.append(nome)
    notas.append(nota)

    continuar = input('Deseja adicionar outro colaborador? (s/n):').lower()
    if continuar == 'n':
      break

# Agora vem a parte analítica

media = sum(notas) / len(notas)
melhor = colaboradores[notas.index(max(notas))]
pior = colaboradores[notas.index(min(notas))]

print('Analisando...')
time.sleep(2)

print('Média Geral da empresa:', media)
print('Melhor Colaborador:', melhor, 'com nota', max(notas))
print('Pior colaborador:', pior, 'com nota', min(notas))

if media >= 8:
   print('Desempenho Geral: Excelente!')
elif media >= 5:
   print('Desempenho Geral: Bom')
else:
    print('Desempenho Geral: Precisa Melhorar')
