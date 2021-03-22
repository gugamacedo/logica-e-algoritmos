algo = input('Digite qualquer coisa: ')
print(f'O tipo primitivo é: {type(algo)}')  # para descobrir o tipo primitivo da variável
print(f'É um número? {algo.isnumeric()}')  # para descobrir se a variável é numérica
print(f'Só tem espaços? {algo.isspace()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está em maiúsculas? {algo.isupper()}')
print(f'Está em minúsculas? {algo.islower()}')
print(f'Está capitalizado? {algo.istitle()}')
