# Faça uma função maior(), que recebe vários parâmetros com valores inteiros e diz qual o maior
from time import sleep
from random import randint

def maior(* num):
    if num == ():
        print('-=-'*10)
        print('Analisando os valores passados...')
        sleep(1.5)
        print(f'Foram informados 0 valores')
        print(f'O maior valor foi 0')
    else:
        print('-=-'*10)
        print('Analisando os valores passados...')
        print('| ', end='')
        sleep(1.5)
        for n in num:
            print(n, end=' | ', flush=True)
            sleep(0.5)
        print(f'Foram informados {len(num)} valores')
        print(f'O maior valor foi {max(num)}')


maior(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
maior(randint(0, 9), randint(0, 9), randint(0, 9))
maior(randint(0, 9), randint(0, 9))
maior(randint(0, 9))
maior()