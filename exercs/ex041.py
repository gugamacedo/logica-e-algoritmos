'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade: até 9 anos mirim, até 14 infantil, até 19 junior, até 24 senior, acima master'''
from datetime import date
yearbirth = int(input('Digite seu ano de nascimento: '))
yearsys = date.today().year
age = yearsys - yearbirth
if age <= 9:
    print(f'Você está na categoria mirim. Vai passar para a categoria infantil daqui {10-age} anos.')
elif age <= 14:
    print(f'Você está na categoria infantil. Vai passar para a categoria júnior daqui {15 - age} anos.')
elif age <= 19:
    print(f'Você está na categoria júnior. Vai passar para a categoria sênior daqui {20 - age} anos.')
elif age <= 24:
    print(f'Você está na categoria sênior. Vai passar para a categoria master daqui {25 - age} anos.')
else:
    print(f'Você está na categoria master.')
