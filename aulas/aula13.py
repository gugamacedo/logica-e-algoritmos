'''
Lembre-se que a variavel do For pode ser manipulada
Vc pode usá-la para especificar um tratamento diferente em algum laço especifico
Pode usar no print para indicar qual o processo atual, diferenciar



# ele para um numero antes, então joga +1 na variavel de fim
# blabla += uhul ao invés de blabla = blabla + uhul


for c in range(1, 7):
for c in range(-7, 1):
for c in range(7, 0, -1):
for c in range(0, 11, 2):
    print(c)
print('Fim')


num = int(input('Digite algum número: '))
# for c in range(0, num+1):
for c in range(0, num+1, 2):
    print(c)
print('Fim')


ini = int(input('Inicio: '))
fim = int(input('Fim: '))
jump = int(input('Passo: '))
for c in range(ini, fim+1, jump):
    print(c, end=' - ')
print('Fim')


s = 0
for c in range(0, 2):
    n = int(input('Digite um número:'))
    s += n
print(s)
'''
