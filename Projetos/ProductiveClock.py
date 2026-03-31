# Sistema de Controle de Tarefas
import os

tarefas = [{'nome': 'Aprender Python', 'concluida': False}]

def exibir_nome_programa():
    print('''ℙ𝕣𝕠𝕕𝕦𝕔𝕥𝕚𝕧𝕖ℂ𝕝𝕠𝕔𝕜''')

def exibir_opcoes():
    print('1 - Adicionar tarefa')
    print('2 - Listar tarefas') 
    print('3 - Sair\n') 

def sair_programa():
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_tarefas():
    exibir_subtitulo('Cadastrar Nova Tarefa')
    nome_tarefa = input('Digite a tarefa que deseja cadastrar: ')
    tarefa = {'nome': nome_tarefa, 'concluida': False}
    tarefas.append(tarefa)
    print(f'A tarefa "{nome_tarefa}" foi cadastrada com sucesso!')

    voltar_ao_menu_principal()

def listar_tarefas():
    exibir_subtitulo('Listando Tarefas')

    print(f"{'Nome da Tarefa'.ljust(30)} | {'Estado'.ljust(20)}")

    for tarefa in tarefas:
        nome_tarefa = tarefa['nome']
        estado = 'Concluída' if tarefa['concluida'] else 'Não finalizada'
        print(f"- {nome_tarefa.ljust(30)} | {estado.ljust(20)}")

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_tarefas()
        elif opcao_escolhida == 2:
            listar_tarefas()
        elif opcao_escolhida == 3:
            sair_programa()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
