'''
- Se você precisar de alguma funcionalidade/módulos amais, você pode importar ima biblioteca (import talbiblioteca).
- Você não precisa importar uma biblioteca inteira, no Python pode usar o from talbiblioteca import talfuncionalidade/módulos
- Pule um linha depois do ‘import’

import math
ceil
floor
trunc
pow
sqrt
factorial

Ceil (arredondar pra baixo), floor (arredondar pra cima), trunc (eliminar os números depois da vírgula),
pow (eliminar os números antes da vírgula), sqrt (raiz quadrada), factorial (fatorial)

from math import sqrt

Se dentro da biblioteca math você quisesse usar apenas o módulo sqrt, pode importar assim.
Se for mais de um módulo, pode adicionar uma vírgula e colocar o próximo

https://docs.python.org/3.8/library/index.html

https://pypi.org/

-----------------------------------------------------------

import math
num = int(input('Digite o núm: '))
print(f'A raiz quadrada de {num} é {math.sqrt(num)}')
print(f'A raiz quadrada de {num} é {math.sqrt(num):.2f}')

from math import sqrt
num = int(input('Digite o núm: '))
print(f'A raiz quadrada de {num} é {sqrt(num)}')

import random
num = random.randint(1, 100)
print(num)

-----------------------------------------------------
import emoji
print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Python is :thumbs_up:', use_aliases=True))
print(emoji.demojize('Python is 👍'))

-----------------------------------------
O Python possui uma função chamada round(). Ela recebe dois parâmetros. O primeiro é o número que você quer arredondar, e o segundo, a quantidade de casas, assim:
round(1.41421356237309, 2)

'''