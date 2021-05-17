'''
# Interactive help
help(print)
print(print.__doc__)



# Docstrings
# é basicamente a documentação de alguma função, a qual vc msm pode criar pras suas funções

def contador(i, f, p):
    """
    -> A funcao faz uma contagem de dezenas
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    @gugamacedo
    """
    for n in range(i, f+1, p):
        print(n)
    print('fim')

# contador(0, 100, 10)
help(contador)



# Funções opcionais
# é diferente do empacotamento da aula passada. Aqui você define quantos parâmetros terão e diz qual os opcionais
def somar(a, b, c=0):  # Aqui eu digo que se nada for passado pro c, ele vale 0
    print(f'A soma é {a+b+c}')

somar(3, 2, 5)
somar(8, 4)



# escopo de variáveis
# define onde a variavel vai ou não existir
# conceito bem maduro no js -> block scope e -> global scope
def teste(b):
    a = 8
    b += 4
    c = 2
    print(f':param a: vale {a}')  # 8
    print(f':param b: vale {b}')  # 9
    print(f':param c: vale {c}')  # 2


a = 5
teste(a)
print(f':param a: vale {a}')  # 5
# quando você tem o parâmetro com o mesmo nome, mas um global e outro em bloco, ele cria as duas variaveis com mesmo nome e com valores diferentes


# tem um jeito de dizer que a variavel será global, mesmo dentro de um bloco (apesar de ser algo raro e geralmente uma péssima ideia, pode acabar atrapalhando outros devs envolvidos no projeto)
# para isso, dentro do bloco você coloca por exemplo: 
def teste(b):  # cuidado que não pode passar uma variavel global no bloco como parâmetro global
    global a
    a = 8
    print(f':param a: vale {a}')  # 8


a = 5
teste(a)
print(f':param a: vale {a}')  # 8 também, pois foi alterada globalmente dentro do bloco
# isso diz que naquele bloco, a variavel deve ser tratada como global ainda 



# Return: retorno de valores
# muito útil para quando você quer apenas retornar valores, sem mensagens repetidas, ou quando quer personalziar melhor
# por retornar valores, você pode jogar a função dentro de uma variável para printar ou manipular do jeito que quiser
def somar(a, b):
    return a+b

# print(somar(1, 2))
soma1 = somar(1, 2)
soma2 = somar(3, 4)
soma3 = somar(5, 6)
print(f'As somas deram: {soma1}, {soma2} e {soma3}')



def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


# num = int(input('Digite um número: '))
# print(f'O fatorial de {num} é {fatorial(num)}')
fatorial1 = fatorial(5)
fatorial2 = fatorial(4)
fatorial3 = fatorial()
print(f'Os fatoriais são {fatorial1}, {fatorial2} e {fatorial3}')

def par_impar(num=0):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
print(f'{num} é par' if par_impar(num) == True else f'{num} é ímpar')
'''
