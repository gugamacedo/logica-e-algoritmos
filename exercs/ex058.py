# Melhore o exer28 onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
# até acertar, mostrando no fim quantos palpites ele precisou
from random import randint
from time import sleep  # essa função faz o código "dormir" por tal tempo
pc = randint(1, 10)  # pc recebendo o número.
print('-=-' * 20)
user = int(input('Adivinhe qual número, de 1 a 10, o PC está pensando: '))  # jogador recebendo o número
while user < 1 or user > 10:
    user = int(input('Adivinhe qual número, de 1 a 10, o PC está pensando: '))
print('Processando...')
sleep(0.5)
stock = 1
while pc != user:
    print(f'Erroooou!')
    if user < pc:
        print('Chuta pra cima...')
    elif user > pc:
        print('Chuta pra baixo...')
    print('-=-' * 20)
    user = int(input('Adivinhe qual número, de 1 a 10, o PC está pensando: '))  # jogador recebendo o número
    print('Processando...')
    sleep(0.5)
    stock += 1
print(f'\033[1;32mParabéns, você acertou, o PC pensou no número {pc}\nVocê precisou de {stock} tentativas.')
