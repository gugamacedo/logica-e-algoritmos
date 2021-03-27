# Crie um programa que leia um  número inteiro e mostre na tela se ele é par ou ímpar
num = int(input('Digite um número para saber se é par ou impar: '))
if num % 2 == 0:  # % é o resto da divisão. Ou seja, divide o número por 2, se a sobra for 0, é par, do contrário ímpar
    print(f'{num} é par')
else:
    print(f'{num} é impar')
