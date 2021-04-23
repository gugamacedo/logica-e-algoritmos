'''
Listas Parte 1 []

Bem parecido com as tuplas, mas a sintaxe é [], e as listas SÃO MUTAVEIS



abc = ['a', 'b', 'c']
print(abc)
abc = ['A', 'B', 'C']
print(abc)
abc += ['D', 'E']
print(abc)



abc = ['a', 'b', 'c']
print(abc)
abc.append('d')  # adiciona ao final da lista
print(abc)
abc += 'e', 'g'
print(abc)
abc.insert(5, 'f')  # insere um item novo, na posição que vc definir
print(abc)
abc.append('h')
print(abc)
abc.pop(7)  # deleta um indice especifico
print(abc)
abc.pop()  # sem nada dentro ele elimina o último indice
print(abc)
# del abc  # elimina
abc.remove('f')  # elimina um conteúdo especifico
print(abc)
if 'e' in abc:  # dá pra usar o if ra eliminar de acordo com a condição
    abc.remove('e')
print(abc)
abc += 'e', 'e'
print(abc)
while 'e' in abc:  # dá pra utilizar while também
    abc.remove('e')
print(abc)
valores = list(range(4, 11, 2))  # pode criar lista com o comando list, dá pra usar range dentro também
print(valores)
lista = [8, 2, 5, 4]
print(sorted(lista))
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
print(len(valores))



lista = [8, 2, 5, 4, 5]
print(lista)
print(lista.count(5))
while 5 in lista:
    lista.remove(5)
    print(lista)
for l in lista:
    print(l, end=' ')
print()
for count in range(0, 3):
    lista.append(int(input('Adicione um valor: ')))
for pos, l in enumerate(lista):
    print(f'Na posição {pos+1} tem o nº{l}')
# quando você copia uma lista, você cria um laço entre eles, se mudar a 2ª, a 1ª também muda
a = [1, 2, 4]
b = a
b.insert(2, 3)
print(f'Lista A {a}\nLista B {b}')
# Pra tirar esse laço e só copiar
b = a[:]
b.insert(0, 0)
print(f'Lista A {a}\nLista B {b}')
'''