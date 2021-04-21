# Leia 4 valores pelo user e guarde-os em uma tupla. Mostre quantas vezes aparece o 9, a posição do 3, e quais são pares
values = (int(input('1º número: ')), int(input('2º número: ')), int(input('3º número: ')), int(input('4º número: ')))
print(f'O número 9 aparece {values.count(9)} vez(es)' if values.count(9) > 0 else 'O nº 9 não aparece!')
print(f'O número 3 está na posição {values.index(3)+1}' if values.count(3) > 0 else 'O nº 3 não aparece!')
print(f'São pares: ', end='')
for val in values:
    if val % 2 == 0:
        print(val, end=' ')
