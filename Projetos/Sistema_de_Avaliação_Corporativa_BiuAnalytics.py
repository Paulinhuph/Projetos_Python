# 💼 Desafio: Sistema de Avaliação Corporativa – BiuAnalytics
import time
print('A empresa BiuAnalytics S.A. utiliza um sistema inteligente para avaliar o desempenho de seus colaboradores e decidir quem será promovido, quem precisa de treinamento e quem será realocado.')
time.sleep(1)
print('Atráves de dados informados irei avaliar o desempenho dos colaboradores.')
time.sleep(1)
print('Com ética profissional, nenhuma das informações recebida serão expostas pela empresa.')
time.sleep(1)
print('______________________________________')
print('Sistema Carregando...')
time.sleep(2)
acessoGerent = (input('Caro Gerente digitar sua senha de acesso:'))

if acessoGerent == '1234':
    print('Acesso Liberado')
    time.sleep(1)
    print('Carregando...')
    nome = input('Digite o nome do colaborador:')
    pont_produt = float(input('Digite a nota de Produtividade(0-100):'))
    pont_comport = float(input('Digite a nota de comportamento Profissional(0-100):'))
    pont_inov = float(input('Digite a nota de Inovação(0-100):'))
    time.sleep(1)
    print('Analisando dados...')
    time.sleep(1)
    if pont_produt >= 85 and pont_comport >= 85 and pont_inov >= 85:
        print('"Colaborador de alta performance. Elegível para promoção imediata."')
    elif pont_produt <= 60 or pont_comport <=60 or pont_inov <= 60:
        print("Desempenho insatisfatório. Recomendado para reavaliação e treinamento.")
    else:
        print('Colaborador com desempenho estável. Manter em observação.')
    
else:
    print('Acesso Negado! Senha incorreta')
