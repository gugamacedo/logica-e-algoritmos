# Igual o 86 mas com novas features:
# A soma de todos pair, a soma da terceira coluna e o maior da segunda linha
matrix = [[], [], []]
stock_pair = 0
# stock_r2 = 0
stock_c3 = 0

for row in range(0, 3):
    for column in range(0, 3):
        matrix[row].append(int(input(f'Digite o valor para [{row}, {column}]: ')))
        if matrix[row][column] % 2 == 0:
            stock_pair += matrix[row][column]
        # if row == 1:
        #     stock_r2 += matrix[row][column]
        #     print('r2')
        if column == 2:
            stock_c3 += matrix[row][column]
print('-=-'*10)
for mx in matrix:
    print(f'[{mx[0]:^5}][{mx[1]:^5}][{mx[2]:^5}]')

print(f'\nA soma de todos os pares: {stock_pair}')
print(f'A soma da coluna 3: {stock_c3}')
print(f'O maior da linha 2: {max(matrix[1])}')
