# O user vai inserir vários nº numa lista. No final exiba essa lista, e outras duas com os nº pares e nº impares
num = []
numpa = []
numim = []
while True:
    num.append(int(input('Digite um número: ')))
    option = str(input('Quer inserir mais um número? [S/N]: ')).upper().strip()
    while 'S' != option != 'N':
        option = str(input('Quer inserir mais um número? [S/N]: ')).upper().strip()
    if option == 'N':
        print(f'\nVocê inseriu os números:', end=' | ')
        for n in num:
            print(n, end=' | ')
            if n % 2 == 0:
                numpa.append(n)
            else:
                numim.append(n)
        print(f'\nSão pares os números:', end=' | ')
        for np in numpa:
            print(np, end=' | ')
        print(f'\nSão ímpares os números :', end=' | ')
        for ni in numim:
            print(ni, end=' | ')
        break
    print()
