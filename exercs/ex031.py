# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas
from time import sleep
distc = float(input('Quantos Kilômetros gastará em sua viagem? '))
print('-=-' * 20, '\nProcessando valor da passagem...')
sleep(3)
print('-=-' * 20)
# preco = distc * 0.50 if distc <= 200 else distc * 0.45
# print(preco) Forma com if simplificado
if distc <= 200:
    print(f'Okay, sua viagem vai custar R${distc * 0.50:.2f}')
else:
    print(f'Okay, sua viagem vai custar R${distc * 0.45:.2f}')
