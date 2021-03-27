# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$5 por cada km acima do limite
from random import randint
from time import sleep
veloci = randint(20, 120)
print('Radar processando sua velocidade...')
sleep(2)
print(f'Você está a {veloci}Km/h')
sleep(2)
if veloci > 80:
    print(f'{veloci - 80}Km/h acima do limite de velocidade!\n'
          f'Vai pagar R${(veloci - 80) * 5} de multa')
else:
    print(f'{80 - veloci}Km/h abaixo do limite de velocidade!')
