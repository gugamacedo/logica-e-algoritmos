'''Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa vai perguntar o 'valor da casa', o 'salário' do comprador e em 'quantos anos' ele pretende pagar
Calcule o 'valor da prestação mensal', sabendo que ela não pode exceder 30% do salário.
Se exceder, o empréstimo deve ser negado'''
from time import sleep
valhouse = float(input('Qual o valor da casa? R$'))
salary = float(input('Qual seu salário mensal? R$')) * 0.30
time = int(input('Em quantos anos pretende pagar o empréstimo? ')) * 12
lending = valhouse/time
print('\nCalculando condições de empréstimo...\n')
sleep(2)
if lending <= salary:
    print(f'\033[1;32mEmpréstimo concedido!\033[m Você vai pagar R${lending:.2f} mensais.')
else:
    print(f'\033[1;31mEmpréstimo negado!\033[m '
          f'Excede 30% do seu salário, nestas condições, com salário a partir de R${lending:.2f}')
