# Faça uma função contador() que receba 3 parâmetros: inicio, meio, fim e realize essas contagens:
# (a) 1 até 10, passo 1     (b) 10 até 0, passo 2       (c) uma contagem escolhida pelo user 
# no (c) caso o user digitar um fim maior que o começo, tem que fazer contagem regressiva. caso o passo seja 0, vira 1
from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio < fim:
        fim +=1
        passo = abs(passo)
    else:
        if passo > 0:
            passo = -passo
        fim -=1
    for n in range(inicio, fim, passo):
        print(n, end=' ', flush=True)
        sleep(0.3)
    print()


contador(1, 10, 1)
contador(10, 0, 2)
print()
inicio = int(input('Digite o o início: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
contador(inicio, fim, passo)
