# Leia seis números inteiros e mostre a soma de todos os que forem pares.
stock = 0
for count in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        stock += num
print('\nSoma dos pares:', stock)
