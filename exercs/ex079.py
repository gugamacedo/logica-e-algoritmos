# Crie um programa onde o user digitado vários valores númericos e cadastre-os em uma lista.
# Caso o número não existe ele não deverá adiciona-lo. No final serão exibidos os números em ordem crescente.
numlist = []
while True:
    num = int(input('\nDigite um número: '))
    # for n in num:  # pensei em usar um for pra validar em loop mas é desnecessario, só usar o IF IN ou IF NOT IN
    if num not in numlist:  # se o num input não está no num lista, ele é adicionado
        numlist.append(num)
        print('Nº adicionado!')
    elif num in numlist:  # se o num input está no num lista aparece essa mensagem e ele não é adicionado
        print('Nº duplicado, não adicionado!')
    option = str(input('Deseja continuar? [S/N] ')).upper()
    while 'S' != option != 'N':
        option = str(input('Deseja continuar? [S/N] ')).upper()
    if option == 'N':
        print('\nVocê digitou os números:', end=' | ')
        for numl in sorted(numlist):  # o sorted só deu aqui, abaixo não
            print(numl, end=' | ')
        break
