# Escreva um programa que faça o computado "pensar" em um número inteiro entre 0 e 5 e peça para o usuário descobrir
# qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
from time import sleep  # essa função faz o código "dormir" por tal tempo
print('-=-' * 20)
user = int(input('Adivinhe qual número, de 1 a 5, o PC está pensando: '))
print('-=-' * 20)
print('Processando...')
sleep(2)
print('-=-' * 20)
pc = randint(1, 5)
if user == pc:
    print(f'Parabés, você acertou, o PC pensou no número {pc}')
else:
    print(f'Erroooou, o PC pensou no número {pc}')
