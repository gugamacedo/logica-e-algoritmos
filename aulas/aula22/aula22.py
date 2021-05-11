'''
# Modularização: 
- Dividir um programa grande
- Organização do código
- Aumentar legibilidade
- Facilitar manutenção
- Ocultação do código detalhado
- Reutilização em outros projetos facilmente
'''
'''
# import funcoes
from funcoes import fatorial, dobro, triplo  # tomar cuidado com esse método, porque o se tiver usando outra lib com o mesmo comando, durante o código pdoe dar confiltos

num = int(input('Digite um número: '))
fatorial = fatorial(num)
dobro = dobro(num)
triplo = triplo(num)

print(f'O fatorial de {num} é {fatorial}')
print(f'O dobro de {num} é {dobro}')
print(f'O triplo de {num} é {triplo}')

'''


'''
Pacotes: caso um módulo fique muito grande, com muitas funções, temos os pacotes
Pacote é uma pasta que contem módulos temáticos
'''

from pacotes import numeros

num = int(input('Digite um número: '))
fatorial = numeros.fatorial(num)
dobro = numeros.dobro(num)
triplo = numeros.triplo(num)

print(f'O fatorial de {num} é {fatorial}')
print(f'O dobro de {num} é {dobro}')
print(f'O triplo de {num} é {triplo}')
