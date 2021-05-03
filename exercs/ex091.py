# 4 jogadores joguem um dado (1-8) e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, e exiba o ranking
from random import randint
from time import sleep
from operator import itemgetter

ranking = {}
for c in range (1, 5):
    ranking[f'Jogador {c}'] = randint(1, 6)

for k, v in ranking.items():
    print(f'{k} tirou 🎲 {v}')
    sleep(0.5)

print(f'\n{"Ranking":^23}\n{"-"*23}')

sorted_ranking = sorted(ranking.items(), key=itemgetter(1), reverse=True) # pra organizar um dicionário. O 1 no itemgetter se refere a localização do value, se fosse 0 pegaria a key
# repare que o dicionário é exibido agora como lista, portanto deve ser tratado como tal
# >>> [('Jogador 4', 6), ('Jogador 2', 3), ('Jogador 1', 2), ('Jogador 3', 2)]

for i, v in enumerate(sorted_ranking):
    print(f'{i+1}º lugar: {v[0]} 🎲{v[1]}')
    sleep(0.5)
