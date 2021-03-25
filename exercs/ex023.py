'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
unidade, centena, dezena, milhar

String Python | zfill ()
O método zfill () retorna uma cópia da string com caracteres '0' preenchidos no lado esquerdo da string especificada.
Sintaxe: str.zfill (length)

num = "0" * (4 - len(num)) + num
print("Unidades: ", num[len(num) - 1])
print("Dezenas: ", num[len(num) - 2])
print("Centenas: ", num[len(num) - 3])
print("Milhar: ", num[len(num) - 4])
'''
num = str(input('Digite um número de 0 a 9999: ')).zfill(4)
print(f'Milhar: {num[0]}\nCentena: {num[1]}\nDezena: {num[2]}\nUnidade: {num[3]}')
