# Leia um número qualquer e mostre seu fatorial. Ex: 5! = 5x4x3x2x1 = 120
from math import factorial
num = int(input('Digite o número e saiba seu fatorial: '))
stock = num
while stock != 0:
    print(f'{stock}', end='')
    print(' * ' if stock > 1 else f' = {factorial(num)}', end='')  # Dá pra colocar if dentro do print
    stock -= 1

