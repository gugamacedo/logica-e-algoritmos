'''
Matriz [[]]
São listas multidimensionais, listas dentro de listas. 

Você acessa primeiro a linha, depois a coluna.
[[2, 4, 6, 8, 10], [1, 3, 5, 7, 9]]
Nessa lista temos duas linhas, 5 colunas em cada. Na primeira linha o números pares, na segunda linha os ímpares.

# pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
# print(pessoas[0][0])
# print(pessoas[1][1])
# print(pessoas[2][0])
# print(pessoas[1])
# count = 0
# for ps in pessoas:
#     for p in ps:
#         count += 1
#         print(p, end=', ' if count % 2 != 0 else '\n')

# teste = []
# teste.append('Loki')
# teste.append(40)
# print(teste)
# galera = []
# galera.append(teste[:]) # não esqueça que o [:] faz uma cópia independente, sem isso fica uma cópia mutua
# print(galera)
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# print(galera[0])
# print(galera[0][0])
# print(galera[2][1])

# for pessoas in galera:
#     print(f'{pessoas[0]} tem {pessoas[1]} anos.')
    
# galera = [] 
# dado = []
# for c in range(0, 3):
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado[:])
#     dado.clear()
# print(galera)

# stockmaior = stockmenor = 0
# for g in galera:
#     if g[1] >= 21:
#         print(f'{g[0]} é MAIOR de idade, tem {g[1]} anos.')
#         stockmaior += 1
#     else:
#         print(f'{g[0]} é MENOR de idade, tem {g[1]} anos.')
#         stockmenor += 1
# print(f'Tem {stockmaior} maiores de idade, e {stockmenor} menores de idade.')
'''