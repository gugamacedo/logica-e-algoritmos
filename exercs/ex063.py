# Leia um número inteiro qualquer e exiba os n primeiros elemtnos de uma sequência de fibonacci. Ex: 0-1-1-2-3-5-8
num1 = 0
num2 = 1
terms = int(input('Quantos termos você deseja ver? '))
count = 2
print(num1, '-', num2, end=' - ')
while count < terms:
    num3 = num1 + num2
    print(num3, ' - ' if count < terms-1 else '', end='')
    num1 = num2
    num2 = num3
    count += 1
    if count == terms:
        terms += int(input('\nDeseja mais quantos termos? '))
