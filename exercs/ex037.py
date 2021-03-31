# Escreva um programa que leia um número inteiro qualquer e peça par o usuário escolher qual será a base de conversão
# 1 para binário, 2 para octal, 3 para hexadecimal
from time import sleep
numint = int(input('Digite um número inteiro qualquer: '))
choice = int(input('( 1 ) para converter para binário!\n'
                   '( 2 ) para converter para octal!\n'
                   '( 3 ) para converter para hexadecimal!\n'
                   'Digite a opção: '))
print('\nEspere um momento para a conversão...')
sleep(2)
if choice == 1:
    print(f'\nO número {numint} em binário é {bin(numint)[2:]}')
elif choice == 2:
    print(f'\nO número {numint} em octal é {oct(numint)[2:]}')
elif choice == 3:
    print(f'\nO número {numint} em hexadeciaml é {hex(numint)[2:]}')
else:
    print(f'\nOpção inválida!')
