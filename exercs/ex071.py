''' Simule o funcionamento de um caixa eletrônico. Primeiro pergunte ao user qual será o valor sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. Obs: apenas cédulas de 1, 10, 20, 50 '''
from time import sleep
cash = int(input('Digite o valor que quer sacar: '))
while cash % 5 != 0:
    cash = int(input('[Apenas valores terminados em 0 ou 5]: '))
print('Gerando saque...')
sleep(1)
count100 = count50 = count20 = count10 = count5 = 0
while True:
    if cash >= 100:
        count100 += 1
        cash -= 100
    elif cash >= 50:
        count50 += 1
        cash -= 50
    elif cash >= 20:
        count20 += 1
        cash -= 20
    elif cash >= 10:
        count10 += 1
        cash -= 10
    elif cash >= 5:
        count5 += 1
        cash -= 5
    elif cash == 0:
        print(f'Saque:', end='')
        print(f'\n{count100} cédula(s) de 100 reais.' if count100 > 0 else '', end='')
        print(f'\n{count50} cédula(s) de 50 reais.' if count50 > 0 else '', end='')
        print(f'\n{count20} cédula(s) de 20 reais.' if count20 > 0 else '', end='')
        print(f'\n{count10} cédula(s) de 10 reais.' if count10 > 0 else '', end='')
        print(f'\n{count5} cédula(s) de 5 reais.' if count5 > 0 else '', end='')
        break
