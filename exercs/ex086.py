# Crie uma matriz 3x3, com os valores que o user inserir
# No final, mostra com a formatação de tabela
matrix = [[], [], []]

for row in range(0, 3):
    for column in range(0, 3):
        matrix[row].append(int(input(f'Digite o valor para [{row}, {column}]: ')))
print('-=-'*10)
for mx in matrix:
    print(f'[{mx[0]:^5}][{mx[1]:^5}][{mx[2]:^5}]')
