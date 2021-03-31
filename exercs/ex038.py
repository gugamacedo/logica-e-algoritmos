# Escreva um programa que leia 'dois números' inteiros e compare-os, monstrando na tela qual o maior, ou se são iguais
num01 = int(input('Bem-vindo ao comparador de números!\n'
                  'Digite o primeiro número: '))
num02 = int(input('Digite agora o segundo número: '))
if num01 > num02:
    print(f'O número {num01} é maior que o número {num02}')
elif num02 > num01:
    print(f'O número {num02} é maior que o número {num01}')
else:
    print('Ambos números são iguais')
