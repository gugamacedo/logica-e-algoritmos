'''
Tuplas (), Listas [], Dicionários {}

    Tuplas (): armazena vários valores. Armazena em Indices numéricos. Durante o fatiamento o útlimo indice não aparece.
    AS TUPLAS SÃO IMUTAVEIS. Não tem editar valores dentro da tupla.

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[0])  # Mostra o hamburguer
print(lanche[2])  # Mostra a pizza
print(lanche[0:2])  # Mostra hamburguer e suco
print(lanche[1:])  # Vai do suco até o final
print(lanche[-1])  # Mostra o último indice, o pudim
print(lanche[-2])  # Mostra o penultimo indice, a Pizza
print(lanche[3])  # Mostra o último indice, o pudim
print(lanche[-3:])  # Mostra o último indice, o pudim
print(len(lanche))  # Mostra o tamanho da variavel, no caso tem 4 valores
for comida in lanche:  # o For não precisa ser usado apenas com range, pode ser usado em variaveis compostas
    print(f'{comida} é incrivel!')
    # Pra cada repetição ele mostra um indice. No ultimo valor ele acaba
for cont in range(0, len(lanche)):
    print(cont, end=') ')
    print(f'{lanche[cont]} é incrivel!')

for pos, comida in enumerate(lanche):  # POS mostra a posição, position
    print(f'{comida} é muito bom! Posição {pos}')

print(sorted(lanche))  # Sorted quer dizer organizado. Aqui mostra em ordem alfabética


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a  # Junta as strings de forma composta, não pelo indice
print(c)
print(len(c))
print(c.count(5))  # conta quantas vezes aparece o 5
print(c.index(2))  # diz qual posição tal número tá. Se colocar 5 ele diz do primeiro 5
print(c.index(5, 1))  # deslocou a pesquisa a partir do valor 1


pessoa = ('Loki', 42, 'H')  # tuplas no python permite tipos diferentes de caracteres
# del pessoa
'''