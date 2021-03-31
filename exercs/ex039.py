'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
Se ele ainda vai se alistar ao serviço militar; Se é a hora de se alistar; Se já passou do tempo do alistamento
Também deverá mostrar o tempo que falta ou que passou do prazo'''
# ano sist - ano nasc = idade, 18 anos, tempo antes ou depois dos 18
from datetime import date
yearsys = date.today().year
dtbirth = int(input('Digite seu ANO de nascimento completo: '))
age = yearsys - dtbirth
if age < 18:
    print(f'Você tem {age} anos. Fará o alistamento militar daqui {18-age} anos, em {yearsys+(18-age)}!')
elif age > 18:
    print(f'Você tem {age} anos. Deveria ter se alistado {age-18} anos atrás, em {yearsys-(age-18)}!')
else:
    print('Você tem que se alistar este ano!')
