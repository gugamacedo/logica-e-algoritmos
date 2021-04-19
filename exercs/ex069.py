''' Cadastro de pessoas: leia a idade e gênero de várias pessoas. Depois pergunte se quer continuar cadastrando,
se quiser faça o mesmo processo. Quando não qusier mais, mostre:
quantas pessoas tem maioridade, quantos homens foram cadastrados e quantas mulheres tem menos de 20 anos '''
countage = countgen = countwomen = 0
while True:
    age = int(input('Digite a idade da pessoa: '))
    if age >= 18:
        countage += 1
    gen = str(input('Digite o gênero da pessoa [H/M]: ')).upper().strip()
    while 'H' != gen != 'M':
        gen = str(input('Digite o gênero da pessoa [H/M]: ')).upper().strip()
    if gen == 'H':
        countgen += 1
    if gen == 'M' and age < 20:
        countwomen += 1
    option = str(input('\nQuer cadastrar mais uma pessoa? [S/N] ')).upper().strip()
    while 'S' != option != 'N':
        option = str(input('Quer cadastrar mais uma pessoa? [S/N] ')).upper().strip()
    if option == 'N':
        print(f'\nTêm {countage} pessoa(s) maior(es) de idade.' if countage > 0 else '', end='')
        print(f'\n{countgen} homens cadastrados.' if countgen > 0 else '', end='')
        print(f'\n{countwomen} mulher(es) com menos de 20 anos.' if countwomen > 0 else '', end='')
        break
