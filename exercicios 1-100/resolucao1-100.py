# Ex 1 -
print('Hello World')

# Ex 2 -
A = 25
B = 25
soma = A + B
print(soma)

# Ex 3
A = float(input('Digite a primeira nota: '))
B = float(input('Digite a segunda nota: '))
media = (A + B) / 2
print(f'A Média do Aluno é {media:1f}')

# Ex 4
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media_n = (n1 + n2 + n3) / 3
print(f'A média das notas é {media_n}')

# Ex 5
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))
valor4 = int(input('Digite o quarto valor: '))
diferenca = (valor1 * valor2) - (valor3 * valor4)
print(diferenca)

# Ex 6
nome = input('Digite seu nome: ')
print(f'Seja Bem-Vindo(a), {nome}!')

# Ex 7
inteiro1 = int(input('Digite o primeiro número: '))
inteiro2 = int(input('Digite o segundo número: '))
somatoria = inteiro1 + inteiro2
print(f'A somátoria entre {inteiro1} e {inteiro2} é {somatoria}')

# Ex 8
nota1 = float(input('Digite a primeira nota do aluno(a) na disciplina: '))
nota2 = float(input('Digite a segunda nota do aluno(a) na disciplina: '))
media_de_notas = (nota1 + nota2) / 2
print(f'A Média do Aluno(a) é: {media_de_notas}')

# Ex 9
numero = float(input('Digite um número: '))
dobro = (numero * 2)
terca_parte = (numero / 3)
print(f'Número: {numero}')
print(f'Dobro: {dobro}')
print(f'Terça parte: {terca_parte}')

# Ex 10
# => m dam hm km
distancia = float(input('Digite a distância em metros: '))
km = distancia / 1000
hm = distancia / 100
dam = distancia / 10
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000
print(f'Metros: {distancia}')
print(f'Quilômetros: {km}')
print(f'Hectômetros: {hm}')
print(f'Decâmetros: {dam}')
print(f'Decímetros: {dm}')
print(f'Centímetros: {cm}')
print(f'Milímetros: {mm}')

# Ex 11
reais = float(input('Digite a quantidade de dinheiro que você tem em (R$): '))
cotacao_dolar = 6
conversao = (reais / cotacao_dolar)
print(f'Total de Dólares que você pode comprar: US$ {conversao:.2f}')

# Ex 12
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
tinta = area / 2
print(f'A aréa a ser Pintada é de: {area} Metros quadrados')
print(f'A quantidade de Tinta necessária é de: {tinta} Litros de tinta')

# Ex 13
preco = float(input('Digite o preço do produto: '))
calculo_desconto = preco * 0.05
aplicando_desconto = preco - calculo_desconto
print(f'O Preço do Produto é: R$ {preco}')
print(f'O Preço Atual com 5 porcento de Desconto é: R${aplicando_desconto:.2f}')

# Ex 14
salario_atual = float(input('Digite o Seu salário Atual para novo reajuste: '))
calculo_novo_salario = salario_atual * 0.15
aplicando_novo_salario = salario_atual + calculo_novo_salario
print(f'Seu Atual salário será de: R$ {aplicando_novo_salario:.2f}')

# Ex 15
carro_km = float(input('Quantos KM o carro percorreu?: '))
carros_dias = int(input('Quantos dias o carro foi alugado?: '))
diaria = 90
km_rodado = 0.20
pagamento_dias = carros_dias * diaria
pagamento_km = carro_km * km_rodado
pagamento_total = pagamento_dias + pagamento_km
print(f'Total Calculado a pagar: R$ {pagamento_total}.')

# Ex 16
dias_trabalhados = int(input('Digite o total de dias trabalhados: '))
carga_horaria = 8
valor_por_hora = 25
valor_total_em_um_dia = valor_por_hora * carga_horaria
valor_total_mes = valor_total_em_um_dia * dias_trabalhados
print(f'O Valor Total do seu salário é de: R$ {valor_total_mes}')

# Ex 17 
cigarros_por_dia = int(input('Quantos cigarros você fuma por dia?: '))
anos_fumados = int(input('Há quantos anos você fuma?: '))
total_dias_fumando = anos_fumados * 365
total_cigarros = cigarros_por_dia * total_dias_fumando
minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / 1440
print(f'O Total de dias Perdidos do Fumante é: {dias_perdidos:.2f}')

# Ex 18 
x = float(input('Digite o valor de X: '))
y = float(input('Digite o valor de Y: '))

if x == 0 and y == 0:
    print(f'Está na Origem.')

elif y == 0:
    print(f'Está no Eixo X')

elif x == 0:
    print('Está no eixo Y')

elif x > 0 and y > 0:
    print('Está no Quadrante 1')

elif x < 0 and y > 0:
    print('Está no Quadrante 2')

elif x < 0 and y < 0:
    print('Está no Quadrante 3')

else:
    print('Está no Quadrante 4')

# Exc 19
print('Prefeitura da Cidade')
print('-' * 50)
kmh_carro = int(input('Digite a Velocidade (Km/h) do carro: '))
if kmh_carro > 80:
    multa_calculo = (kmh_carro - 80) * 5.00
    print('Você ultrapassou a velocidade máxima da via (80km/h).')
    print(f'Você foi multado. Valor: R$ {multa_calculo}')
else: 
    print('Velocidade ideal.')
    print('Sem multa.')

# Ex 20
nome_aluno = input('Digite o Nome do Aluno(a): ')
nota_do_aluno1 = float(input('Digite a Nota do Aluno(a): '))
nota_do_aluno2 = float(input('Digite a Nota do Aluno(a): '))
media_nota_do_aluno = (nota_do_aluno1 + nota_do_aluno2) / 2

if media_nota_do_aluno >= 7.0:
    print(f'Aprovado! O Aluno(a) {nome_aluno} teve um bom aproveitamento.')
    print(f'Média: {media_nota_do_aluno:.2f}')

else:
    print(f'O Aluno(a) {nome_aluno} não teve um bom aproveitamento. Reprovado!')
    print(f'Média: {media_nota_do_aluno:.2f}')

# Exc 21
num_1 = int(input("Digite o Primeiro Número: "))

if num_1 % 2 == 0:
    print(f'O número {num_1} é PAR')
else: 
    print(f'O número {num_1} é ÍMPAR')


# Exc 22

ano_bi = int(input("Digite um ano: "))
if (ano_bi % 4 == 0 and ano_bi % 100 != 0) or (ano_bi % 400 == 0):
    print(f'O ano {ano_bi} é bissexto.')
else:
    print(f'O ano {ano_bi} não é bissexto.')

# Exc 23 

percurso_km = int(input('Digite a distância que você deseja percorrer (KM): '))
if percurso_km <= 200:
    calculo_passagem = percurso_km * 0.50
    print(f'O Valor da Passagem é de: R$ {calculo_passagem:.2f}')

elif percurso_km > 200:
    calculo_passagem = percurso_km * 0.45
    print(f'O Valor da sua passagem é de: R$ {calculo_passagem:.2f}')


# Exc 24

print('-- Reajuste Salarial --')
print('-' * 50)
nome_func = input('Digite seu nome: ')
salario_func = float(input('Digite seu Salário: '))
anos_trabalhados = int(input('Digite seu tempo na empresa (Anos): '))

if anos_trabalhados <= 3:
    reajuste_calculo = salario_func * 0.03
    reajuste_novo_salario = salario_func + reajuste_calculo
    print(f'Você teve um reajuste de 3%: R${reajuste_calculo}')
    print(f'Com o reajuste seu salário atual será: R$ {reajuste_novo_salario:.2f}')

elif 3 < anos_trabalhados < 10:
    reajuste_calculo = salario_func * 0.125
    reajuste_novo_salario = salario_func + reajuste_calculo
    print(f'Você teve um reajuste de 12.5%: R${reajuste_calculo}')
    print(f'Com o reajuste seu salário atual será: R$ {reajuste_novo_salario:.2f}')

else:
    reajuste_calculo = salario_func * 0.20
    reajuste_novo_salario = salario_func + reajuste_calculo
    print(f'Você teve um reajuste de 20%: R${reajuste_calculo}')
    print(f'Com o reajuste seu salário atual será: R$ {reajuste_novo_salario:.2f}')

# Exc 25 
print('-- Avaliador de IMC --')
peso = float(input('Digite o seu Peso Corporal (KG): '))
altura = float(input('Digite a sua altura (METROS): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Abaixo do Peso. IMC: {imc:.2f}')
elif 18.5 <= imc < 25:
    print(f'Peso ideal. IMC: {imc:.2f}')
elif 25 <= imc < 30:
    print(f'Sobrepeso. IMC: {imc:.2f}')
elif 30 <= imc < 40:
    print(f'Obesidade. IMC: {imc:.2f}')
else:
    print(f'Obesidade Mórbida. IMC: {imc:.2f}')

# Exc 26
print('--- Ediney Automóveis ---')

tipo = input('Qual foi o carro escolhido (Popular/Luxo): ').lower()
km = float(input('Digite a quantidade de quilômetros percorridos (KM): '))
dias = int(input('Digite o total de dias de aluguel: '))

if tipo == 'popular':
    custo_diaria = dias * 90
    
    if km <= 100:
        custo_km = km * 0.20
    else:
        custo_km = km * 0.10

elif tipo == 'luxo':
    custo_diaria = dias * 150
    
    if km <= 200:
        custo_km = km * 0.30
    else:
        custo_km = km * 0.25

total = custo_diaria + custo_km

print(f'Gasto com a diária: R$ {custo_diaria:.2f}')
print(f'Gasto por Km percorrido: R$ {custo_km:.2f}')
print(f'O gasto total será: R$ {total:.2f}')

# Exc 27

horas_esporte = int(input('Quantas horas você práticou de atividade física esse mês? '))

if horas_esporte < 10:
    calculo_ponto = horas_esporte * 2 
    calculo_dinheiro = calculo_ponto * 0.05
    print(f'Parabéns! Você ganhou R$ {calculo_dinheiro:.2f}.')
    print(f'Seu total de Pontos: {calculo_ponto:.2f}')
    

elif 10 > horas_esporte <= 20:
    calculo_ponto = horas_esporte * 5
    calculo_dinheiro = calculo_ponto * 0.05
    print(f'Parabéns! Você ganhou R$ {calculo_dinheiro:.2f}.')
    print(f'Seu total de Pontos: {calculo_ponto:.2f}')

elif horas_esporte > 20:
    calculo_ponto = horas_esporte * 10
    calculo_dinheiro = calculo_ponto * 0.05
    print(f'Parabéns! Você ganhou R$ {calculo_dinheiro:.2f}.')
    print(f'Seu total de Pontos: {calculo_ponto:.2f}')

    
# Exc 28
# range(inicio, fim, passo)
soma = 0
for i in range(6, 101, 2):
    soma += i
    
print(soma)

# Exc 29
# Se você quer descer de 500 até 0, o passo precisa ser negativo:
soma = 500
for i in range (500, 0, -50):
    soma += i
print(soma)

# Exc 30
# Lê o valor inicial da contagem
# input() retorna string, então usamos int() para converter para número inteiro
inicio = int(input("Valor inicial: "))
# Lê o valor final da contagem
fim = int(input("Valor final: "))
# Lê o incremento (de quanto em quanto a contagem anda)
incremento = int(input("Incremento: "))


# Verificação crítica: incremento não pode ser zero
# Porque uma contagem com passo 0 nunca avança (loop inválido)
if incremento == 0:
    print("Incremento não pode ser zero.")
else:
    # Aqui o programa decide a DIREÇÃO da contagem
    # Caso 1: contagem crescente (ex: 1 até 10)
    if inicio < fim:
        # range(inicio, fim + 1, incremento)
        # fim + 1 porque o range NÃO inclui o valor final
        for i in range(inicio, fim + 1, incremento):
            # end=" " evita quebra de linha e imprime tudo na mesma linha
            print(i, end=" ")
    # Caso 2: contagem decrescente (ex: 10 até 1)
    else:
        # Aqui precisamos inverter o sinal do incremento
        # porque estamos descendo (passo negativo)
        for i in range(inicio, fim - 1, -incremento):
            # fim - 1 pelo mesmo motivo: garantir inclusão do valor final
            print(i, end=" ")

# Exc 31

# Variável vazia que vai guardar o total acumulado, começando do zero
soma = 0
# Repete o bloco de código exatamente 7 vezes
for i in range(7):
    # Pede um npumero ao usuário e converte em inteiro
    numero = int(input('Digite o número: '))
    # Soma o número digitado ao total acumulado em soma 
    soma += numero

print(soma)
# Exibe o resultado total da soma após 7 repetições

# Exc 32
def Gerador(): # Define um procedimento chamado hello que não recebe parãmetros
    print('-' * 10)
    print('Olá, Mundo!') # Mensagem principal
    print('-' * 10)

Gerador()

# Exc 33
def Gerador(nome):
    print('-' * 10)
    print('Olá', nome) # Mensagem principal
    print('-' * 10)

Gerador('Paulo') # Se a função pede algo → você precisa entregar algo.
    
# Exc 34 
pi = 3.14159 # Define o valor fixo de pi
raio = float(input('Digite o raio: ')) # Lê o valor do raio digitado pelo usuário e converte para inteiro
area_circulo = pi * raio ** 2 # Calcula a área elevando o raio ao quadrado e multiplicando por pi
print(f'Cálculo da área: {area_circulo:.2f}') # Mostra o resultado formatado com 2 casas decimais

# Exc 35

# 1. DEFINIÇÃO (A Planta da Máquina)
# Criamos a função antes de usá-la. 'a' e 'b' aqui são PARAMETROS.
# Eles funcionam como "espaços reservados" para os dados que virão de fora.
def somador(a, b):
    soma = a + b      # Processamento interno (ocorre na memória local)
    return soma       # O 'braço mecânico' que devolve o resultado para o programa

# 2. COLETA DE DADOS (A Matéria-Prima)
# O float() converte o texto do input em números decimais (Cálculo Numérico).
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# 3. EXECUÇÃO E CAPTURA (Ligar a Máquina)
# Chamamos a função passando 'valor1' e 'valor2' como ARGUMENTOS.
# A variável 'v_soma' RECEBE o que a função 'cuspir' no return.
v_soma = somador(valor1, valor2)

# 4. SAÍDA (O Produto Final)
# Exibimos o resultado que agora está salvo com segurança na variável externa.
print(f"O valor da soma é {v_soma}")

# Exc 36

# 1. ENTRADA DE DADOS
# Usamos float() para aceitar números decimais (ex: 10.5 metros)
largura_terreno = float(input('Digite a Largura: '))
comprimento_terreno = float(input('Digite o comprimento do terreno: '))

# 2. CÁLCULO (PROCESSAMENTO)
# Aqui a variável 'calculo_area' armazena o resultado da multiplicação
calculo_area = largura_terreno * comprimento_terreno

# 3. LÓGICA DE DECISÃO (CONDICIONAIS)
# O Python testará as condições de cima para baixo até encontrar uma VERDADEIRA.

if calculo_area < 100:
    # Este bloco só executa se a área for estritamente menor que 100
    print(f'Área: {calculo_area:.2f} m².') # :.2f formata para 2 casas decimais
    print('Classificação: Terreno Popular.')

elif 100 <= calculo_area <= 500:
    # O 'elif' (else if) só é testado se a condição de cima for FALSA.
    # Aqui verificamos se a área está no intervalo entre 100 e 500.
    print(f'Área: {calculo_area:.2f} m².')
    print('Classificação: Terreno Master.')

else:
    # O 'else' é o caminho padrão. Se não for < 100 e não estiver entre 100 e 500,
    # matematicamente só pode ser acima de 500.
    print(f'Área: {calculo_area:.2f} m².')
    print('Classificação: Terreno VIP.')


# Exc 37

# O range(30, 0, -1) funciona como uma contagem de tempo:
# 30: Início da contagem.
# 0:  Ponto de parada (exclusivo, então o último número será 1).
# -1: O passo (step), que subtrai 1 a cada volta do laço.
for numero in range(30, 0, -1):
    # O operador '%' (módulo) calcula o resto da divisão.
    # Se o resto de um número dividido por 4 é ZERO, ele é múltiplo de 4.
    if numero % 4 == 0:
        # Se a condição for VERDADEIRA, executamos este bloco:
        print(f"{numero} [Divisível por 4]")
    
    else:
        # Se a condição for FALSA (qualquer outro resto), executamos este:
        print(f"{numero}")


# Exc 38

# 1. ENTRADA DE DADOS (CONTEXTO GLOBAL)
# Coletamos os valores antes de chamar a função.
n1_base = int(input("Digite o número da base: "))
n2_expoente = int(input("Digite o número do expoente: "))

# 2. DEFINIÇÃO DA FUNÇÃO (A FERRAMENTA)
# 'n1_base' e 'n2_expoente' aqui são PARAMETROS (portas de entrada).
def potencial(base, expoente):
    """
    Realiza o cálculo de base elevada ao expoente.
    Matematicamente: resultado = base^expoente
    """
    exponenciacao = base ** expoente
    return exponenciacao

# 3. CHAMADA E EXECUÇÃO
# Passamos os valores digitados para a função e guardamos o retorno.
resultado = potencial(n1_base, n2_expoente)

# 4. EXIBIÇÃO (RESULTADO FINAL)
# O :.2f formata para duas casas decimais, útil caso a base seja decimal.
print(f"O Resultado da Exponenciação é: {resultado:.2f}")

# Exc 39

# 1. INICIALIZAÇÃO (O CONTADOR)
# Começamos em zero porque, antes de olhar os números, não encontramos nenhum par.
cont_pares = 0

# 2. REPETIÇÃO (O LAÇO)
# O range(5) fará o bloco interno rodar 5 vezes (0, 1, 2, 3, 4).
for i in range(5):
    # Coletamos o dado e convertemos para inteiro (int)
    number = int(input("Digite o Número: "))
    
    # 3. FILTRO DE PARIDADE
    # O operador % 2 verifica se o resto da divisão por 2 é zero.
    if number % 2 == 0:
        # Se for par, o contador ganha +1 (Incremento)
        cont_pares += 1

# 4. EXIBIÇÃO DO RELATÓRIO (FORA DO LAÇO)
# O print está fora da indentação do 'for', logo, só aparece no final de tudo.
print(f"Ao todo, foram digitados {cont_pares} números pares.")

# Exc 40

nome = input("Digite o seu nome: ")
genero = input("Digite o seu Gênero (M/F): ").upper() # Padronizamos para maiúsculo
valor_compras = float(input("Digite o Valor Total da Compra: "))

# 1. DEFINIÇÃO DA REGRA DE NEGÓCIO
# Isolamos apenas a variável que muda: o percentual de desconto.
if genero == "F":
    porcentagem = 0.13  # 13%
    print(f"\n-- Feliz Dia das Mulheres, {nome}! --")
else:
    porcentagem = 0.05  # 5% 
    print(f"\nOlá, {nome}!")

# 2. CÁLCULO 
desconto = valor_compras * porcentagem
total_pagar = valor_compras - desconto

# 3. EXIBIÇÃO ÚNICA (SAÍDA)
print(f"Desconto aplicado: {porcentagem*100:.0f}%")
print(f"Total da Compra: R$ {valor_compras:.2f}")
print(f"Total a Pagar: R$ {total_pagar:.2f}")

# Exc 41 
# ENTRADA
nome = input("Digite o seu nome: ")
genero = input("Gênero (M/F): ").upper()
salario = float(input("Salário atual: R$ "))
tempo = int(input("Anos de empresa: "))

# PROCESSAMENTO: DEFINIÇÃO DA TAXA
# Usamos os blocos apenas para "escolher" o número da porcentagem
if genero == "F":
    if tempo < 15:
        porcentagem = 0.05
    elif 15 <= tempo <= 20: # Lógica de intervalo corrigida
        porcentagem = 0.12
    else:
        porcentagem = 0.23
else:
    if tempo < 20:
        porcentagem = 0.03
    elif 20 <= tempo <= 30: # Lógica de intervalo corrigida
        porcentagem = 0.13
    else:
        porcentagem = 0.25

# CÁLCULO ÚNICO (Fora dos IFs de gênero)
aumento = salario * porcentagem
novo_salario = salario + aumento

# SAÍDA ÚNICA
print("-" * 30)
print(f"Colaborador(a): {nome}")
print(f"Reajuste aplicado: {porcentagem*100:.0f}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")

# Exc 42

# 1. Camada de Entrada (Input)
inicio = int(input("Valor inicial: "))
fim = int(input("Valor final: "))
incremento = int(input("Incremento: "))
# 2. Camada de Sanitização (Tratamento do Dado)
# Removemos o sinal do usuário. O controle direcional agora é do sistema.
incremento = abs(incremento)
# Trava de segurança contra Loop Infinito (Divisão por zero lógica)
if incremento == 0:
    incremento = 1
    print("[Aviso do Sistema] Incremento zero detectado. Ajustado automaticamente para 1.")
# 3. Camada de Execução (Motor Lógico)
if inicio < fim:
    # Cenário A: Contagem Crescente
    # range(start, stop, step) -> O 'stop' não é inclusivo, por isso fim + 1
    for i in range(inicio, fim + 1, incremento):
        print(i, end=" ")
else:
    # Cenário B: Contagem Decrescente
    # Como garantimos que 'incremento' é positivo na linha 10, '-incremento' sempre subtrairá.
    for i in range(inicio, fim - 1, -incremento):
        print(i, end=" ")

    
# Exc 43

    # 1. INICIALIZAÇÃO (O CONTADOR)
# Começamos em zero porque, antes de olhar os números, não encontramos nenhum par.
cont_pares = 0
cont_impares = 0
# 2. REPETIÇÃO (O LAÇO)
# O range(6) fará o bloco interno rodar 6 vezes (0, 1, 2, 3, 4, 5).
for i in range(6):
    # Coletamos o dado e convertemos para inteiro (int)
    number = int(input("Digite o Número: "))
    # 3. FILTRO DE PARIDADE
    # O operador % 2 verifica se o resto da divisão por 2 é zero.
    if number % 2 == 0:
        # Se for par, o contador ganha +1 (Incremento)
        cont_pares += 1
    else: # Se não for par, o contador ganha +1 (Incremento)
        cont_impares += 1
# 4. EXIBIÇÃO DO RELATÓRIO (FORA DO LAÇO)
# O print está fora da indentação do 'for', logo, só aparece no final de tudo.
print(f"Ao todo, foram digitados {cont_pares} números pares.")
print(f"Ao todo, foram digitados {cont_impares} números ímpares.")


# Exc 44
# Inicialização de uma estrutura de dados do tipo Lista (Vetor)
lista_nome = []
# Primeiro bloco: Coleta de Dados (Complexidade O(n))
# Este laço se repetirá exatamente 7 vezes (índices 0 a 6)
for i in range(7):
    # Interação com o usuário para captura de string
    nome = input("Digite o Nome: ")
    # Método append: insere o elemento no final da lista, na memória RAM
    lista_nome.append(nome)
# Segundo bloco: Exibição Inversa (Algoritmo de Retrocesso)
# O range começa em 6 (último índice), vai até -1 (exclusivo, para parar no 0)
# O passo -1 indica que a contagem é regressiva
for i in range(6, -1, -1):
    # Esta linha acessa o valor, mas não executa saída (operação redundante)
    lista_nome[i]
    # A função print acessa o conteúdo da 'gaveta' i e exibe no console
    print(lista_nome[i])


# Exc 45
# --- DEFINIÇÃO DA FUNÇÃO (A Ferramenta) ---
# A função media é um "contrato": ela promete receber dois valores e devolver um.
def media(nota_1, nota_2):
    # Processamento: Cálculo da média aritmética simples.
    # O uso de parênteses garante a precedência da soma sobre a divisão.
    calculo = (nota_1 + nota_2) / 2
    # Retorno: A função "morre" aqui e entrega o resultado para quem a chamou.
    return calculo
# --- PROGRAMA PRINCIPAL (A Execução) ---
# Entrada de dados com coerção de tipo (casting) para float.
# Fundamental para aceitar valores como 7.5 ou 8.0.
nota_1 = float(input("Digite a Primeira nota: "))
nota_2 = float(input("Digite a Segunda nota: "))
# Invocação da Função:
# Aqui, os valores das variáveis nota_1 e nota_2 são "copiados" para dentro da função.
resultado = media(nota_1, nota_2)
# Saída de Dados Formatada:
# O especificador :.2f limita a dízima decimal a duas casas, mantendo o rigor científico.
print(f"O resultado da Média foi: {resultado:.2f}")


# Exc 46
# Definição do Procedimento: Recebe a String e o Inteiro
def gerador(msg, num):
    # O motor de repetição: i assumirá valores de 0 até (num - 1)
    for i in range(num):
        # Acesso direto ao conteúdo da variável msg
        print(msg)
# Programa Principal: Coleta de dados
# O input sempre retorna string, por isso o 'int()' é obrigatório para o número
msg = input("Digite a Mensagem a ser repetida: ")
num = int(input("Digite o Número de repetição: "))
# Chamada do Procedimento:
# Note que não precisamos de 'resultado =' porque a função não retorna valor, ela apenas age.
gerador(msg, num)


# Exc 47
# DEFINIÇÃO DO PROCEDIMENTO
def maior(valor1, valor2):
    # estrutura de Decisão: O coração da lógica booleana
    if valor1 < valor2:
        print(f"O maior valor é {valor2}")
    elif valor1 > valor2:
        print(f"O maior valor é {valor1}")
    else:
        # Tratamento da Exceção: valores idênticos
        print(f"Os valores são iguais.")
    # Um procedimento de exibição não precisa retornar a si mesmo.
    # return valor1, valor2 <==
# Programa Principal
# Coleta de dados com tipagem inteira para comparação matemática
valor1 = int(input("Digite o Primeiro Valor: "))
valor2 = int(input("Digite o Segundo Valor: "))
# Chamada direta do procedimento
maior(valor1, valor2)


# Exc 48 
# Definição do Procedimento: Recebe um inteiro como argumento
def parouimpar(number):
    # Operação de Módulo: verifica o resto da divisão por 2
    if number % 2 == 0:
        # Se o resto é zero, a condição booleana é Verdadeira
        print("O número é par.")
    else:
        # Caso contrário, por exclusão lógica, o número é ímpar
        print("O número é ímpar.")
# Entrada de Dados: Conversão explícita para Inteiro
number = int(input("Digite o Número: "))
# Chamada do Procedimento: Passagem do parâmetro por valor
parouimpar(number)


# Exc 49
# Definição da Função (Motor de Cálculo)
def calculopontos(vitoria, empate, derrota):
    # Processamento: A derrota multiplica por 0, logo é irrelevante para a soma
    # mas mantê-la no pensamento lógico ajuda na clareza do algoritmo.
    pontuacao = (vitoria * 3) + (empate * 1)
    # RETORNO: A função encerra e devolve o valor para o programa principal 
    return pontuacao
# Programa Principal (A Interface com o Usuário)
vitoria = int(input("Digite o Número de Vitórias: "))
empate = int(input("Digite o Número de Empates: "))
derrota = int(input("Digite o Número de Derrotas: "))
# Chamada da Função capturando o valor retornado
total = calculopontos(vitoria, empate, derrota)
# agora o programa principal decide o que fazer com o "total"
print(f"O número total de pontos é {total}")


# Exc 50

# DEFINIÇÃO DA FUNÇÃO: Focada em uma única responsabilidade
def quadrado(number):
    # Processamento: Elevação à segunda potência
    calculo_quadrado = number ** 2
    # RETORNO: Entrega o resultado técnico para o chamador
    return calculo_quadrado
# PROGRAMA PRINCIPAL
# Captura de entrada (Casting para Inteiro)
number = int(input("Digite um Número: "))
# Atribuição do retorno à variável 'resultado'
resultado = quadrado(number)
# Saída formatada (Exibição do dado processado)
print(f"O Quadrado do Número {number} é {resultado}")


# Exc 51

# DEFINIÇÃO DA FUNÇÃO: Conversor de Grandeza Escalar
def conversao(minutos_entrada):
    # Processamento: Razão matemática (1h / 60min)
    # Dividir minutos por 60 isola a grandeza "Hora"
    calculo_h = minutos_entrada / 60
    # RETORNO: Devolve o valor real (float) para o programa principal
    return calculo_h
# PROGRAMA PRINCIPAL
# Entrada: O usuário fornece a base de cálculo
min = int(input("Digite o Valor em Minutos para a Conversão: "))
# Chamada e Atribuição: O 'resultado' agora carrega a precisão decimal
resultado_em_horas = conversao(min)
# Saída: Exibição com máscara de duas casas decimais
print(f"{min} minutos é equivalente a {resultado_em_horas:.2f} horas.")


# Exc 52

# DEFINIÇÃO: Função de vizinhança aritmética
def antesuc(numero):
    # Processamento: Definição dos limites imediatos
    antecessor = numero - 1
    sucessor = numero + 1
    # Saída Interna: Informa o usuário imediatamente
    print(f"O Antecessor de {numero} é {antecessor}")
    print(f"O Sucessor de {numero} é {sucessor}")
    # RETORNO MÚLTIPLO: Devolve ambos os valores como uma Tupla
    return antecessor, sucessor
# PROGRAMA PRINCIPAL
numero = int(input("Digite um número: "))
# Chamada da função: Aqui 'resultado' armazena (n-1, n+1)
resultado = antesuc(numero)


# Exc 53

# DEFINIÇÃO: Função matemática pura
def dobro(numero):
    # O processamento ocorre isolado do mundo exterior
    calculo = numero * 2
    # A entrega do dado: A função termina e "se transforma" no valor resultante
    return calculo
# PROGRAMA PRINCIPAL: Gestão de Interface
# Entrada de dados (Input + Casting)
numero = int(input("Digite um Número: "))
# Chamada e Atribuição: O valor retornado preenche a variável 'resultado_final'
resultado_final = dobro(numero)
# Exibição: O programa principal decide como o usuário verá o dado
print(f"O Dobro de {numero} é {resultado_final}")


# Exc 54

# --- DEFINIÇÃO DAS FUNÇÕES (As Regras de Negócio) ---
def para_dolar(reais, taxa):
    return reais / taxa
def para_real(dolar, taxa):
    return dolar * taxa
# --- CONFIGURAÇÕES GLOBAL ---
TAXA_CAMBIO = 6.00
# --- PROGRAMA PRINCIPAL ---
print("1- Real para Dólar \n2- Dólar para Real")
escolha = input("Escolha a opção (1/2): ")
if escolha == "1":
    v = float(input("Valor em R$: "))
    resultado = para_dolar(v, TAXA_CAMBIO)
    print(f"Resultado: US$ {resultado:.2f}")
elif escolha == "2":
    v = float(input("Valor em US$: "))
    resultado = para_real(v, TAXA_CAMBIO)
    print(f"Resultado: R$ {resultado:.2f}")


# Exc 55
def calcular_valor(tipo_texto):
    if tipo_texto == "algum_texto":
        return 100 # Retorna um número baseado no texto acima
    elif tipo_texto == "outro_texto":
        return 200
    else:
        return 0
    

# Exc 56
def simulacao_impostor(n_impostores, n_jogadores):
    # Processamento: Razão entre subconjunto e conjunto total
    # Multiplicar por 100 converte a frequência relativa em porcentagem
    calculo = (n_impostores / n_jogadores) * 100
    # RETORNO: O valor percentual "limpo" para o programa principal
    return calculo
# PROGRAMA PRINCIPAL
# Entrada de dados quantitativos
i = int(input("Quantos Impostores terão na Partida?: "))
j = int(input("Quantos jogadores terão na Partida?: "))
# Chamada da função: Passagem de argumentos por posição
chance = simulacao_impostor(i, j)
# Exibição: Formatação com duas casas decimais para precisão científica
print(f"A chance de ser impostor nesta configuração é: {chance:.2f}%")


# Exc 57
# DEFINIÇÃO: Função de conversão composta
def calculador_dias(anos, meses, dias):
    # Processamento: Conversão de Anos (Constante 365)
    calculo_a = anos * 365
    # Processamento: Conversão de Meses (Média 30)
    calculo_m = meses * 30
    # Síntese: Soma de todas as unidades convertidas
    total_geral = calculo_a + calculo_m + dias
    return total_geral
# PROGRAMA PRINCIPAL
# Coleta de dados (Entradas discretas)
anos = int(input("Digite quantos anos você tem: "))
meses = int(input("Digite quantos meses: "))
dias = int(input("Digite quantos dias: "))
# Execução: A função recebe 3 argumentos e retorna 1 valor
resultado_final = calculador_dias(anos, meses, dias)
# Saída: Exibição do acumulado temporal
print(f"Sua idade expressa em dias é: {resultado_final}")


# Exc 58
biblioteca = {}
def cadastrar_livro(dicionario, nome, livro):
    # Usamos 'dicionario' (o parâmetro), não a variável global
    if nome in dicionario:
        dicionario[nome].append(livro)
    else:
        # Criação da lista inicial para o novo usuário
        dicionario[nome] = [livro]
    # Não precisamos de return, pois dicionários são alterados por referência
    
def obter_livros(dicionario, nome):
    # Verificamos se a chave existe no armário
    if nome in dicionario:
        # Retornamos apenas o conteúdo daquela chave (a lista de livros)
        return dicionario[nome]
    else:
        # Em vez de apenas imprimir, retornamos uma lista vazia para evitar erros futuros
        return []
# --- O MOTOR DE CADASTRO ---
while True: 
    nome = input("Digite o Nome da Pessoa: ")
    livro = input("Digite o Nome do Livro que ela leu: ")
    
    # Chamada CORRETA: Passando a biblioteca e os dados lidos
    cadastrar_livro(biblioteca, nome, livro)
    
    deseja_continuar = input("Deseja Continuar Cadastrando? (s/n): ").lower().strip()
    if deseja_continuar in ["n", "não", "nao"]:
        break
# --- A ETAPA DE CONSULTA (O GRANDE FINAL) ---
print("--- CONSULTA DE LEITURAS ---")
busca = input("De quem você deseja ver a lista de livros? ")

# Aqui usamos a sua SEGUNDA função (obter_livros)
meus_livros = obter_livros(biblioteca, busca)

if meus_livros:
    print(f"Livros lidos por {busca}: {meus_livros}")
else:
    print(f"Nenhum registro encontrado para {busca}.")


# Exc 59
lista_semana = ["Domingo", "Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado"]
entrada = int(input("Digite o Número Inteiro (1-7): "))
if 1 <= entrada <= 7:
    # Fazemos o cálculo e guardamos na variável 'indice'
    indice = entrada - 1
    # Usamos a variável para imprimir uma única mensagem clara
    print(f"O Dia correspondente é: {lista_semana[indice]}")
else:
    print("Valor Inválido! Por favor, escolha entre 1 e 7.")


# Exc 60
# Esta função recebe três argumentos e os mapeia para variáveis locais
def contador(inicio, fim, incremento):
    """
    Realiza uma contagem aritmética baseada em parâmetros.
    O 'fim + 1' garante que o limite superior seja inclusivo.
    """
    # O laço 'for' utiliza a função range() para gerar a sequência
    # A estrutura é: range(ponto_de_partida, ponto_de_parada, passo)
    for i in range(inicio, fim + 1, incremento):
        # Exibição de cada iteração na tela
        print(i)
# --- PROGRAMA PRINCIPAL (Interface com o Usuário) ---
# Coleta de dados quantitativos com conversão de tipo (casting para int)
inicio = int(input("Valor inicial: "))
fim = int(input("Valor final: "))
incremento = int(input("Incremento: "))
# --- A CHAMADA (Invocação do Procedimento) ---
# Aqui, enviamos as variáveis 'inicio', 'fim' e 'incremento' para a função.
# O Python "pula" para a linha 3, executa o código e depois retorna para cá.
contador(inicio, fim, incremento)


# Exc 61
def inteiro(numero): # Procedimento de validação de conjunto numérico
    # Lógica de Resto: Se a divisão por 1 for exata, não há decimais
    if numero % 1 == 0:
        print(f"O Número {numero} é inteiro.")
    else:
        print("O Número não é inteiro")
# Usamos float() no input para permitir que o usuário digite pontos decimais
numero = float(input("Digite o Número: "))
# Chamada do procedimento
inteiro(numero)


# Exc 62
lista_nomes = []
def ordenacao(lista_nomes):
    lista_nomes.sort()
# --- BLOCO DE COLETA ---
while True: 
    # .strip() remove espaços inúteis e .title() padroniza a capitalização
    nome = input("Digite o Nome: ").title().strip()
    # ADICIONAMOS PRIMEIRO para garantir que o dado entre na lista
    lista_nomes.append(nome)
    deseja_continuar = input("Deseja adicionar mais algum nome? (sim/não): ").lower()
    if deseja_continuar == "não":
        break
# --- BLOCO DE PROCESSAMENTO (Eficiência: Ordenamos apenas uma vez ao final) ---
ordenacao(lista_nomes)
# --- BLOCO DE EXIBIÇÃO ---
print("-- Lista De Pessoas Ordenadas --")
for nome in lista_nomes:
    print(nome)


# Exc 63
# Criamos uma lista vazia para armazenar a série histórica de preços
lista_produto = []
# --- CAPTURA DO MARCO ZERO (1º PRODUTO) ---
# Lemos o primeiro valor fora do laço para servir de referência inicial
# Sem isso, não teríamos com o que comparar o segundo produto.
preco = float(input("Digite o Preço do Produto: "))
 # Estratégia de Atribuição Inicial:
# No primeiro produto, o maior e o menor são, necessariamente, o mesmo valor.
maior = preco
menor = preco
# --- LAÇO DE REPETIÇÃO (PRODUTOS 2 A 8) ---
# Como já lemos 1 produto, o range(7) completará o ciclo de 8 entradas.
for i in range(7):
    # Captura dos preços subsequentes
    preco = float(input("Digite o Preço do Produto: "))
    # Alimentação da Lista: Armazenamos o valor para análise posterior
    lista_produto.append(preco)
    # Lógica de Comparação Independente (Estrutura If-Elif):
    # Se o preço atual superar o recorde, atualizamos o 'maior'.
    if preco > maior:
        maior = preco
    # Caso contrário, verificamos se ele é inferior ao recorde de 'menor'
    elif preco < menor:
        menor = preco
# --- EXIBIÇÃO DOS RESULTADOS (MÉTODOS NATIVOS) ---
# Aqui você utiliza as funções built-in do Python que percorrem a lista
# e retornam os valores extremos encontrados.
print(f"O Maior preço encontrado na lista foi: {max(lista_produto)}")
print(f"O Menor preço encontrado na lista foi: {min(lista_produto)}")


# Exc 64
# Inicialização do Acumulador
soma = 0 
# Laço de Repetição Indefinida
while True:
    # Captura do Dado como Inteiro (Rigor de Tipagem)
    numero = int(input("Digite um Número: "))
    # Verificação de Sentinela
    if numero == 1111:
        break
    # Acumulação (Soma Progressiva)
    # Esta linha só é alcançada se o "if" acima for falso
    soma = soma + numero
# Exibição do Somátorio
print(f"O Somátorio Final foi de: {soma:.2f}")


# Exc 65
def maior(numero1, numero2, numero3):
    # Técnica do Líder Provisório
    maior = numero1
    if numero2 > maior:
        maior = numero2
    if numero3 > maior:
        maior = numero3
    return maior # Retorna o Dado para o programa principal
# Programa Principal
numero1 = int(input("Digite o Primeiro Valor: "))
numero2 = int(input("Digite o Segundo Valor: "))
numero3 = int(input("Digite o Terceiro Valor: "))
# Chamada da Função e guardamos o resultado em uma variável
resultado = maior(numero1, numero2, numero3)
print(f"Entre os valores, o maior é: {resultado}")


# Exc 66
# Motor de cálculo
def supersomador(n1, n2):
    soma_total = 0
    for i in range(n1, n2 + 1):
        soma_total = soma_total + i
    return soma_total
# Programa Principal
n1 = int(input("Digite um Valor: "))
n2 = int(input("Digite um Valor: "))
# Chamada e Armazenamento
resultado = supersomador(n1, n2)
# Exibição formatada
print(f"A Soma de todos os valores no Intervalo é {resultado}")


# Exc 67

def media(nota_1, nota_2):
    calculo = (nota_1 + nota_2) / 2
    return calculo
nota_1 = float(input("Digite a Primeira nota: "))
nota_2 = float(input("Digite a Segunda nota: "))

resultado_calculo = media(nota_1, nota_2)

def situacao(resultado_calculo):
    if resultado_calculo >= 7:
        return "Aprovado"
    elif 5 <= resultado_calculo < 7:
        return "Recuperação"
    else:
        return "Reprovado"
    
resultado_situacao = situacao(resultado_calculo)

print(f"O Resultado da Média foi: {resultado_calculo}")
print(f"Situação Do Aluno: {resultado_situacao}")


# Exc 68
# Definição de uma função variádica: o '*' empacota argumentos em uma tupla
def somadorpassado(*numeros):
    # Utiliza a função built-in sum() para processar a iterável 'numeros'
    return sum(numeros)
# Inicialização de uma estrutura de dados do tipo Lista (mutável) para persistência
lista_valores = []
# Estrutura de repetição de fluxo contínuo (Laço Infinito controlado)
while True:
    # Entrada de dados com coerção de tipo (casting) para Inteiro
    # Nota: Se o input não for numérico, haverá uma interrupção por ValueError
    numeros = int(input("Digite um Número: "))
    # Método de lista para anexar o valor ao final da coleção, preservando dados anteriores
    lista_valores.append(numeros)
    # Captura da condição de parada e normalização da string para caixa baixa
    deseja_continuar = input("Deseja adicionar mais algum número? (sim/não): ").lower()
    # Sentença condicional para quebra do fluxo de repetição
    if deseja_continuar == "não":
        break
# Invocação da função com 'Splat Operator' (*) para desempacotar a lista em argumentos individuais
resultado_final = somadorpassado(*lista_valores)
# Definição de uma função de saída de dados (Interface com o usuário)
# Nota: O parâmetro 'somadorpassado' aqui está sombreado (shadowing) e não é utilizado no corpo
def exibir(somadorpassado):
       # Exibição de string formatada (f-string) acessando uma variável de escopo global
       print(f"O Total Somado foi de: {resultado_final}") 
# Chamada da função de exibição passando a referência da função original como argumento
exibir(somadorpassado)


# Exc 69 
# Definição da Função com parâmetros posicionais
def contar_letra(texto, letra): 
    # Count: contar a frequência de um elemento específico dentro de uma estrutura de dados
    return texto.lower().count(letra.lower()) 
# Programa Principal
texto = input("Digite o Texto desejado: ")
letra = input("Digite a Letra: ")
# Guarda o resultado da função
resultado = contar_letra(texto, letra)
# Exibe o resultado
print(f"O Número de vezes que a Letra - '{letra.upper()}' - aparece no texto é: {resultado}")


# Exc 70
for n in range(1, 20):
    # Condição de Maior Precedência:
    # Verificamos a divisibilidade cumulativa (3 E 5) antes das individuais.
    # Se invertermos essa ordem, o número 15 seria capturado pelo 'n % 3', gerando um erro lógico.
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    # Condição Alternativa 1:
    # Se não for múltiplo de ambos, testamos se é divisível estritamente por 3.
    elif n % 3 == 0:
        print("Fizz")
    # Condição Alternativa 2:
    # Se falhar nos anteriores, testamos a divisibilidade por 5.
    elif n % 5 == 0:
        print("Buzz")
    # Cláusula de Escape (Default):
    # Se o número não atender a nenhum critério aritmético acima, 
    # o fluxo cai no 'else' e imprime o valor original.
    else:
        print(n)


# Exc 71
# Definindo a função com parâmetro de início da contagem
def contadorreverso(numero):
    # Range (inicio, fim e passo)
    # Começa no número, vai até -1 para que o 0 seja incluido
    for n in range(numero, -1, -1):
        print(n)
# Programa Principal: Entrada de Dados
numero = int(input("Digite um Número: "))
# Chamada da Função
contadorreverso(numero)
# Exibição
print("Contagem Finalizada!")

# Exc 72
import random
# Definição da função de processamento lógico
def comparando(computador, jogador):
    # Caso de Empate: A condição mais simples e rápida de processar
    if jogador == computador: 
        return 'Empate!'
    # Casos de Vitória do Jogador: Agrupados com o operador 'or'
    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'papel' and computador == 'pedra') or \
         (jogador == 'tesoura' and computador == 'papel'):
        return 'Vitória do Jogador!'
    # Caso de Vitória do Computador: Por exclusão lógica.
    else:
        return 'Vitória do Computador!'
# --- Fluxo Principal do Sistema ---
opcoes = ['pedra', 'papel', 'tesoura']
computador = random.choice(opcoes)
jogador = input('Digite uma opção: (Pedra/Papel/Tesoura): ').lower().strip()
print('-' * 5, 'Joken-PO' '-' * 5)
print(f'Computador escolheu: {computador.upper()}')
print(f'Você escolheu: {jogador.upper()}')
resultado = comparando(computador, jogador)
print(f'RESULTADO FINAL: {resultado}')


# Exc 73
# Lista original de dados "sujos" (com maiúsculas e minúsculas)
lista = ['Banana', 'Maça', 'Uva', 'Abacaxi', 'Abacate']
lista_convertida_minuscula = [s.lower() for s in lista]
def verificacao(lista_convertida_minuscula, elemento):
    # O operador 'in' verifica a existência do elemento na sequência.
    if elemento in lista_convertida_minuscula:
        return f'O elemento {elemento.capitalize()} encontrado na Lista!'
    else:
        return f'O elemento {elemento.capitalize()} não está na Lista!'
# Entrada de dados com saneamento (remover espaços e padronizar caixa)
elemento = input('Digite o Nome de uma Fruta: ').lower().strip()
# Chamada da função passando a lista bruta e o alvo
resultado = verificacao(lista_convertida_minuscula, elemento)
print(resultado)


# Exc 74
import random
# Função com Responsabilidade Única: Apenas gerar os dados
def jogardado():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    msg1 = f"O Primeiro Dado obteve número: {dado1}"
    msg2 = f"O Segundo Dado obteve número: {dado2}"
    return dado1, dado2, msg1, msg2
# Função de Processamento Matemático
def soma(d1, d2):
    return d1 + d2
# --- Camada de Execução e Interface (I/O) ---
valor_dado1, valor_dado2, mensagem1, mensagem2 = jogardado()
resultado_soma = soma(valor_dado1, valor_dado2)
print(mensagem1)
print(mensagem2)
print(f'A Soma dos valores dos Dados foi: {resultado_soma}')

# Exc 75
senha_correta = "admin"
tentativas = 0
acesso_concedido = False # Flag de estado (Booleano)
while tentativas < 3:
    # Captura e saneamento de dados
    digite_a_senha = input("Digite a Senha: ").lower().strip()
    if digite_a_senha == senha_correta:
        acesso_concedido = True
        print(f"Sucesso!")
        break # Interrupção imediata do fluxo
    else:
        tentativas +=1
        # Feedback dinâmico de tentativas restantes
        print("Erro! Senha Incorreta, tente novamente.")
        print(f"Tentativas Restante: {3 - tentativas}")
# --- Tratamento Pós-Laço ---
if acesso_concedido:
    print("Bem-vindo, Administrador.")
else:
    print("\n[ALERTA] 3 tentativas incorretas. Sua conta foi BLOQUEADA por segurança.")

# Exc 76 
# Cálculo Matemático
def calculo_idade(ano_nascimento,ano_atual):
    calculo = ano_atual - ano_nascimento
    return calculo
# Responsabilidade Única - Decisão Lógica (Pode ou Não)
def votar(resultado):
    # O enunciado pede para mostrar se pode ou não.
    print(f"Sua idade Atual é: {resultado} anos.")
    if resultado >= 18:
        print(f"Você Pode Votar!")
    else: 
        print("Você ainda não pode votar!")
# --- Entrada de Dados (Interface) ---
ano_atual = int(input("Digite o Ano Atual: "))
ano_nascimento = int(input("Digite o seu Ano de Nascimento: "))
# Processamento
resultado = calculo_idade(ano_nascimento,ano_atual)
# Saída de Dados
votar(resultado)


# Exc 77
# Inicialização de Variáveis (Estado Inicial do Sistema)
soma = 0
cont_18 = 0
cont_5 = 0
maior = 0
# Estrutura de Repetição com Contador (Lote de 10)
for i in range(1, 11):
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    # 1. Acumulador: Soma o valor atual ao valor que já estava na 'caixinha'
    soma += idade
    # 2. Contadores de Categoria (Uso de IFs independentes)
    # Verificamos cada critério sem que um anule o outro.
    if idade > 18:
        cont_18 += 1
    if idade < 5:
        cont_5 += 1
    # 3. Lógica de Máximo: Atualiza a variável 'maior' apenas se o novo dado 
    # for superior ao atual recorde.
    if idade > maior:
        maior = idade
# Processamento Final (Aritmética de Agregação)
media = soma / 10
# Interface de Saída (Saída de Dados Formatada)
print(f"a) Média de Idade: {media:.1f} anos.")
print(f"b) Pessoas com mais de 18: {cont_18}")
print(f"c) Pessoas com menos de 5: {cont_5}")
print(f"d) Maior idade lida: {maior}")


# Exc 78
soma = 0
const_h = 0
soma_idade_h = 0
const_m = 0
m_maiores_20 = 0
media_h = 0
for i in range(1,6):
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    sexo = input(f"Digite o Sexo da {i}ª pessoa (masculino/feminino): ").lower().strip()
    # Acumulador para a média geral do grupo
    soma += idade
    if sexo == "masculino":
        const_h += 1
        soma_idade_h += idade # Acumula idade apenas de homens

    elif sexo == "feminino":
        const_m += 1
        # Regra de negócio específica: Mulheres com mais de 20 anos
        if idade > 20:
            m_maiores_20 += 1
# --- Processamento dos Dados Agregados ---
media_grupo = soma / 5
# Proteção contra divisão por zero (Caso não haja homens cadastrados)
if const_h > 0:
    # A média é SOMA dividida pela QUANTIDADE
    media_h = soma_idade_h / const_h
else:
    media_h = 0
# --- Interface de Saída (Output) ---
print(f"a) Total de Homens Cadastrados: {const_h}")
print(f"b) Total de Mulheres Cadastradas: {const_m}")
print(f"c) A Média do Grupo: {media_grupo:.1f} anos.")
print(f"d) A Média dos Homens: {media_h:.1f} anos.")
print(f"e) Mulheres com idade Acima de 20 anos: {m_maiores_20}")
        

# Exc 79
# Inicialização de Acumuladores e Contadores (Estado Zero)
pessoas_kg_90 = 0
pessoas_50_160 = 0
pessoas_190_100 = 0
soma_total_altura = 0
# Laço de Repetição (Input em Lote)
for i in range(1, 6):
    # Coleta de Dados Individuais
    peso = float(input(f"Digite o peso (KG) da {i}ª pessoa: "))
    altura = int(input(f"Digite a altura (CM) da {i}ª pessoa: "))
    # Acumulando a altura para o cálculo da média do grupo
    soma_total_altura += altura
    # b) Classificação por peso individual
    if peso > 90:
        pessoas_kg_90 += 1
    # c) Filtro Composto: Peso E Altura (Ambos devem ser verdadeiros)
    if peso < 50 and altura < 160:
        pessoas_50_160 += 1
    # d) Filtro Composto de Alta Performance: Altura E Peso
    if altura > 190 and peso > 100:
        pessoas_190_100 += 1
# Cálculo da Média (Operação de Agregação realizada após a coleta)
media_altura = soma_total_altura / 5
# Saída de Dados (Interface com o Usuário)
print("-" * 30)
print(f"a) Média de Altura do Grupo: {media_altura:.2f} cm")
print(f"b) Pessoas acima de 90kg: {pessoas_kg_90}")
print(f"c) Pessoas com menos de 50kg e menos de 160cm: {pessoas_50_160}")
print(f"d) Pessoas com mais de 190cm e mais de 100kg: {pessoas_190_100}")


# Exc 80
# Inicialização dos Acumuladores Financeiros
salario = 0
salario_h = 0
salario_m = 0
while True:
    # 1. Entrada de Dados (Saneamento com float e lower/strip)
    salario = float(input("Digite o Salário: "))
    sexo = input("Digite o gênero (feminino/masculino): ").lower().strip()
    deseja_adicionar = input("Deseja Adicionar mais? (sim/não): ").lower().strip()
    # 2. Processamento de Regras de Negócio (Acúmulo por Categoria)
    if sexo == "masculino":
        salario_h += salario
    elif sexo == "feminino":
        salario_m += salario
    # 3. Condição de Saída (Sentinela)
    if deseja_adicionar == "não":
        break
# --- Relatório Final (Interface de Saída) ---
print("-" * 30)    
print(f"RELATÓRIO DE FOLHA DE PAGAMENTO")
print(f"Total do Salário dos Homens: {salario_h:.2f}")    
print(f"Total do Salário das Mulheres: {salario_m:.2f}")


# Exc 81
total_alunos = 0
total_notas = 0
print("-- Sistema de Registro de Notas --")
print("--- Para interromper digite a nota 999. ---")
while True:
    nota = float(input("Digite a nota do Aluno: "))
    if nota == 999:
        break
    total_alunos += 1 
    total_notas += nota
# --- Relatório Final (Interface de Saída) ---
if total_alunos > 0:
    media_total = total_notas / total_alunos
    print("-" * 35)
    print(f"RELATÓRIO DE NOTAS")
    print(f"Total de Alunos na Turma: {total_alunos}")
    print(f"Média do Grupo: {media_total:.2f}")
else: 
    print("Nenhuma Nota foi registrada.")


# Exc 82
total_homens = 0
idade_homens = 0
idade_mulheres = []
todas_idades = []
while True:
    sexo = input("Digite o Gênero (masculino/feminino): ").lower().strip()
    idade = int(input("Digite a idade: "))
    todas_idades.append(idade)
    if sexo == "masculino":
        idade_homens += idade
        total_homens += 1
    elif sexo == "feminino":
        idade_mulheres.append(idade)
    deseja_continuar = input("Deseja adicionar mais? (sim/não): ").lower().strip()
    if deseja_continuar == "não":
        break
print("-" * 35)
print("RELATÓRIO FINAL")
# a) Maior idade lida (Protegido: só executa se houver idades)
if todas_idades:
    print(f"a) Maior idade lida: {max(todas_idades)} anos.")
# b) Total de homens
print(f"b) Homens cadastrados: {total_homens}")
# c) Mulher mais jovem (Protegido contra lista vazia)
if idade_mulheres:
    print(f"c) Idade da mulher mais jovem: {min(idade_mulheres)} anos.")
else:
    print("c) Nenhuma mulher foi cadastrada.")
# d) Média dos homens (Protegido contra divisão por zero)
if total_homens > 0:
    media_h = idade_homens / total_homens
    print(f"d) Média de idade dos homens: {media_h:.1f} anos.")
else:
    print("d) Média de idade dos homens: N/A (Sem homens).")


# Exc 83 