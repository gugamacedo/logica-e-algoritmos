# Refaça o exer 51 com while
print('10 termos de uma PA\n')
firsterm = int(input('Digite o 1º termo da Progressão aritmética: '))
reason = int(input('Digite a constante da PA: '))
count = 0
while count < 10:
    print(firsterm, end='')
    print(' - ' if count < 9 else '', end='')
    firsterm += reason
    count += 1
