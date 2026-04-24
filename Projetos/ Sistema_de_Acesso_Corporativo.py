# 💼 Desafio: Sistema de Acesso Corporativo
print('💼 Implementamos um novo sistema de acesso corporativo')
print('Vamos verificar sua identidade e permissões')
import time
print('AGUARDE...')
print('----------------------------------------------------')
time.sleep(4)

username = input('Digite seu nome:')
cargo = (input('Digite seu cargo (Gerente, Funcionário, Estagiário):')).lower()
senha = int(input('Digite sua senha de acesso:'))

# as senhas dos gerentes são (5000); dos funcionários (3333) e dos estagiários (1111)

if senha == 5000 or cargo == 'gerente':
    print('Bem Vindo, Gerente', username + '!')
    print('O sistema está liberado! Bom trabalho!')
elif senha == 3333 or cargo == 'funcionário':
    print('Acesso negado! Funcionário', username + 'Você não tem acesso a essa página do sistema.')
elif senha == 1111 or cargo == 'estagiário':
    print('Acesso negado! Estagiário', username + '⚠️ Credenciais inválidas. Contate o administrador de TI.')
