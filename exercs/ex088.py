# Mega Sena: o programa vai perguntar quantos jogos 0 user que gerar, serão sorteados 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma matriz, sem repetição dentro de cada jogo.
from time import sleep
from random import randint

matrix = []

print(' Mega Sena Generator')
print('-=-'*7)
option = int(input('Quantos jogos você que gerar? '))
print('-=-'*11)

for j in range(option): # esse é o laço dos Jogos
    matrix.append([]) # aqui você vai adicionando o jogo a cada laço, -vazio-
    for n in range(0, 6): # laço dos números, 6 no caso
        random_num = randint(1, 60)
        # o J é muito útil para usar como indice da lista atual
        while random_num in matrix[j]: # caso o número aleatório já exista na lista atual, ele procura outro
            random_num = randint(1, 60) 
        matrix[j].append(random_num) # ainda dentro do laço dos números, você adiciona o número a lista atual
    matrix[j].sort() # só pra organizar a lista interna
    sleep(0.5)
    print(f'Jogo {j+1}: {matrix[j]}')
