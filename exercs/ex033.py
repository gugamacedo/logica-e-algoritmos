# Faça um programa que leia três números e diga qual o maior e o menor
num1 = int(input('Diga o 1º número: '))
num2 = int(input('Diga o 2º número: '))
num3 = int(input('Diga o 3º número: '))
# Jeito mais simples de comparar
if num1 > num2 and num1 > num3:
    maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print(f'O maior número é o {maior}\n'
      f'O menor número é o {menor}')
