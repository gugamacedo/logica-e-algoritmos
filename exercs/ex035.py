# Desenvolva um programa que leia 3 comprimentos de retas e diga ao usuário se elas podem ou não formar um triângulo
# Principio matemático do triângulo
num1 = float(input('Diga o tamanho da 1ª reta: '))
num2 = float(input('Diga o tamanho da 2ª reta: '))
num3 = float(input('Diga o tamanho da 3ª reta: '))
# if num1 - num2 < num3 < num1 + num2 or num2 - num3 < num1 < num2 + num3 or num1 - num3 < num2 < num1 + num3:
if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    print(f'Dá pra montar um triângulo')
else:
    print(f'Num dá não')
