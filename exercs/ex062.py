# Melhore o exer 061, perguntando se o user quer mostrar mais alguns termos após o 10ºO programa acaba qdo ele inserir 0
from time import sleep
print('10 termos de uma PA\n')
firsterm = int(input('Digite o 1º termo da Progressão aritmética: '))
reason = int(input('Digite a constante da PA: '))
print()
count = 0
countuser = 10
while count < countuser:
    print(firsterm, end='')
    print(' - ' if count < countuser-1 else '', end='')
    firsterm += reason
    count += 1
    if count == countuser:
        print()
        countuser += int(input('\nVocê quer inserir mais quantos termos? '))
sleep(1)
print('\nPrograma finalizado')
