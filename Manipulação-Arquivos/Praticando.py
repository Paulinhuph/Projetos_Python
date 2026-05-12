# Crie um programa que grave em um arquivo alunos.csv uma lista de alunos e suas notas.
# Leia o arquivo alunos.csv e imprima apenas os alunos com nota maior ou igual a 7.0.
import os
import csv

with open('alunos.csv', 'w', newline='') as f:
    escritor = csv.writer(f)
    escritor.writerow(['aluno', 'nota'])
    escritor.writerow(['Ana Martins Ribeiro', 7.5])
    escritor.writerow(['Paulo Henrique Farias', 8.5])
    escritor.writerow(['Lucas Portugal Novaes', 9.5])
    escritor.writerow(['Arthur Aguir Simões', 5.6])
    escritor.writerow(['Cintia Moraes Azevedo', 4.5])
    escritor.writerow(['Karina Melo Silva', 6.3])

with open('alunos.csv', 'r', newline='', encoding='utf-8') as f:
        leitor = csv.reader(f)
        next(leitor)

        for linha in leitor:
            nome = linha[0]
            nota = float(linha[0])

            if linha >= 7:
                  print(f"Aluno: {nome} | Nota: {nota}")
