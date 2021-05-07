# Crie uma lista chamada 'números' e duas funções: sorteia(), que vai sortear 5 números e colocá-los dentro da lista, e soma_par() que vai mostrar a soma entre todos números pares da função anterior
# não tem muita necessidade da primeira função, o sample() já faz isso
from random import sample
from time import sleep

def sorteia(numeros):
    print('Sorteando os 5 valores da lista: ', end='', flush=True)
    for n in numeros:
        sleep(1)
        print(n, end=' ', flush=True)
    print()

def soma_par(numeros):
    print('Somando os valores pares: ', end='', flush=True)
    tot_par = 0
    for n in numeros:
        if n % 2 == 0:
            sleep(1)
            print(n, end=' ', flush=True)
            tot_par += n
    sleep(1)
    print(f'resulta em  {tot_par}')
    print()


numeros = sample(range(1, 10), 5)
numeros.sort()
sorteia(numeros)
soma_par(numeros)
