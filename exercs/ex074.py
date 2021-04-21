# Gere 5 nºs aleatórios e coloque em uma tupla. Depois mostre qual o maior e menor valores sorteados
from random import randint
# num = tuple(sample(range(10), 5))
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for n in num:
    print(n, end=' ')
print(f'\nO maior valor é {max(num)}\nO menor valor é {min(num)}')
