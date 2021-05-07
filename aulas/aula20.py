'''
Funções Parte 1

Funções são boas pra trabalhar com block scope, e pra realizar não repetir rotinas no código

def lin():  # definindo a função
    print('-=-'*10)

lin()  # chamando a função, não precisa de print
print('Aprenda Python')
lin()
lin()
print('Estude Python')
lin()
lin()
print('Respire Python')
lin()


# Parâmetro: extremamente importante. Quando você tem apenas um pedaço que muda, ao invés de fazer hardcoded, você pode tornar mais dinâmico através de um parâmetro, alterando apenas está parte do código. Veja exemplo abaixo: 
def mensagem(texto):
    print('-=-'*10)
    print(texto)
    print('-=-'*10)

mensagem('Aprenda Python')
mensagem('Estude Python')
mensagem('Respire Python')


# Interagindo parâmetros
def soma(a , b):
    s = a + b
    print(f'A soma de {a} + {b} é {s}')

soma(1, 1)
soma(2, 2)
soma(3, 3)


# empacotamento * : quando você não tem  um limite de quantos parâmetros o user pode passar na saída
# o parâmetro empacotado vira tupla ( e adquire todos métodos das tuplas)
def contador(*num):
    # for valor in num:
    #     print(valor, end=' ')
    # print('fim')
    tam = len(num)
    print(f'Recebi {tam} valores: {num}')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos +=1

valores = [6, 3, 9, 1, 0 ,2]
dobra(valores)
print(valores)


def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
    print(sum(valores))

soma(5, 2)
soma(2, 9, 4)
'''
