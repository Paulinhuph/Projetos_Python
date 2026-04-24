import os
import time

def iniciar_programa():
    print('''𝒑𝒍𝒂𝒕𝒂𝒇𝒐𝒓𝒎𝒂 𝒅𝒆 𝒎𝒐𝒏𝒊𝒕𝒐𝒓𝒂𝒎𝒆𝒏𝒕𝒐 𝒐𝒃𝒔𝒕𝒆𝒕𝒓𝒊𝒄𝒐''')
    time.sleep(1)
    print('Olá Colaborador!')
    print('O sistema irá carregar...')
    time.sleep(1)
    print('Aguarde!')
    time.sleep(1)
    print('Tudo Pronto!')
    print('ABBA Maternidade Estadual ⚕')
    print('_' * 35)


def cadastrar_quantidades_de_partos():
    partos_por_mes = []

    partos_por_mes.append(int(input('Digite o número de partos do mês (Janeiro): ')))
    partos_por_mes.append(int(input('Digite o número de partos do mês (Fevereiro): ')))
    partos_por_mes.append(int(input('Digite o número de partos do mês (Março): ')))
    partos_por_mes.append(int(input('Digite o número de partos do mês (Abril): ')))
    partos_por_mes.append(int(input('Digite o número de partos do mês (Maio): ')))
    partos_por_mes.append(int(input('Digite o número de partos do mês (Junho): ')))
    partos_por_mes.append(int(input('Digite o número de partos do mês (Julho): ')))
    partos_por_mes.append(int(input('Digite o número de partos do mês (Agosto): ')))
    partos_por_mes.append(int(input('Digite o número de partos do mês (Setembro): ')))
    partos_por_mes.append(int(input('Digite o número de partos do mês (Outubro): ')))
    partos_por_mes.append(int(input('Digite o número de partos do mês (Novembro): ')))
    partos_por_mes.append(int(input('Digite o número de partos do mês (Dezembro): ')))

    return partos_por_mes


def calcular_total_partos(partos_por_mes):
    return sum(partos_por_mes)


def exibir_partos_mensais(partos_por_mes, total_partos):
    print('\nRelatório Anual de Partos')
    print('-' * 35)

    meses = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ]

    for mes, quantidade in zip(meses, partos_por_mes):
        print(f'{mes}: {quantidade} partos')

    print(f'\nTotal anual de partos: {total_partos}')
    print(f'Média mensal: {total_partos / 12:.2f}')


def normal_ou_cesarea():
    parto_normal = int(input('Digite quantos foram partos normais no ano: '))
    parto_cesariana = int(input('Digite quantos foram partos cesarianos no ano: '))
    return parto_normal, parto_cesariana


def main():
    os.system('cls')
    iniciar_programa()

    partos_por_mes = cadastrar_quantidades_de_partos()
    total_partos = calcular_total_partos(partos_por_mes)

    exibir_partos_mensais(partos_por_mes, total_partos)

    parto_normal, parto_cesariana = normal_ou_cesarea()

    print('\nResumo Final')
    print('-' * 35)
    print(f'Partos normais: {parto_normal}')
    print(f'Partos cesarianos: {parto_cesariana}')


if __name__ == '__main__':
    main()
