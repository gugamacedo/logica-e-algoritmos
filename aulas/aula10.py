'''
estruturas condicionais simples e compostas
== !=
Só if, condicional simples
if e else, condicional composta

if carro.esquerda():
    bloco True
else:
    bloco False

indetação alianhada a esquerda executa independente do que for
    indetação pra dentro, executa dependendo das condições

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo hein')
else:
    print('Carro velho hein')
print('--FIM--')
print('Carro novo' if tempo <= 3 else 'Carro velho')  # forma simplificada, operador ternário

nome = str(input('Qual seu nome? '))
print(f'Bom dia, {nome}')
if nome == 'Gertrude':
    print('Nome lindo..bem moderno')
else:
    print('Nome bobo...normie')

n1 = float(input('Digite nota 1: '))
n2 = float(input('Digite nota 2: '))
nm = (n1+n2)/2
if nm >= 6:
    print('Você passou de ano!!!')
else:
    print('Você é o vergonha do profisson!')
print(f'Sua média foi {round(nm, 2)}')
print('Parabéns' if nm >= 6 else 'Estude mais')  # Operador ternário
'''
