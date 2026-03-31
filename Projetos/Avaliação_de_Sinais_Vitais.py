# 🩺 Exercício de Lógica de Programação — Avaliação de Sinais Vitais;
# O Hospital JJMS quer criar um pequeno sistema que registre os sinais vitais de um paciente na triagem e emita um alerta de risco conforme os valores medidos. 
import time
print('\033[4;31;44mSistema-de-Triagem-Hospital-JJMS.\033[m')
print('Aferição SSVV')
time.sleep(1)
from datetime import datetime
agora = datetime.now()
print(agora.strftime("%d/%m/%Y %H:%M"))
time.sleep(1)
nome = input('Digite o Nome do Paciente: ')
idade = int(input('Digite a idade do Paciente: '))
time.sleep(1)
print('-' * 70)
time.sleep(1)
print('Carregando Sistema de SSVV...')
time.sleep(1)
fc = int(input('Digite a quantidade de batimentos por minuto: '))
pressao_arterial_sistolica = int(input('Digite a Pressão Arterial Sistólica (MMHG): '))
pressao_arterial_diastole = int(input('Digite a Pressão Arterial Diastólica (MMHG): '))
temperatura = float(input('Digite a temperatura em (Celsius): '))
time.sleep(1)
# Agora vem o relatório da triagem:
time.sleep(1)
from datetime import datetime
agora = datetime.now()
print(agora.strftime("%d/%m/%Y %H:%M"))
print('\033[4;31;44mRelátorio-de-Triagem-Hospital-JJMS.\033[m')
time.sleep(1)
print('Nome do Paciente: {}'.format(nome))
time.sleep(1)
print('A idade é: {}'.format(idade))
if idade < 18:
    print('Paciente Menor de idade: {} anos'.format(idade))
else:
    print('Paciente Maior de idade: {} anos.'.format(idade))
time.sleep(1)

# SSVV: FC:
if fc < 60:
    print('Bradicardia {} FC.'.format(fc))
elif fc > 100:
    print('Taquicardia {} FC.'.format(fc))
else:
    print('Frequência Cardíaca Normal {} FC'.format(fc))

# SSVV: Pressão Arterial:
if pressao_arterial_sistolica < 120 and pressao_arterial_diastole < 80:
    print('Hipotensão:', pressao_arterial_sistolica,'x',pressao_arterial_diastole,'mmHg.')
elif pressao_arterial_sistolica > 140 and pressao_arterial_diastole > 90:
    print('Hipertensão:',pressao_arterial_sistolica,'x',pressao_arterial_diastole,'mmHg.')
else:
    print('Normotensão:',pressao_arterial_sistolica,'x',pressao_arterial_diastole,'mmHg.')

# SSVV: Temperatura:
if 36 <= temperatura <= 36.9:
    print('Temperatura Normal: {} °C.'.format(temperatura))
elif temperatura < 36:
    print('Hipotermia: {} °C'.format(temperatura))
elif temperatura > 37:
    print('Hipertermia: {} °C'.format(temperatura))
time.sleep(1)

print('-' * 75)
print('Encerrando-Triagem')
