# Leia vários números e coloque numa lista. Mostre quantos números foram inseridos, a lista em ordem decrescente,
# e se tem ou não o valor 5, e em qual posição.
num = []
while True:
    num.append(int(input('Digite um número: ')))
    option = str(input('Quer inserir mais um número?[S/N]: ')).upper().strip()
    while 'S' != option != 'N':
        option = str(input('Quer inserir mais um número?[S/N]: ')).upper().strip()
    if option == 'N':
        print(f'\nVocê inseriu {len(num)} números:', end=' | ')
        for n in reversed(sorted(num)):
            print(n, end=' | ')
        print(f'\nO nº 5 foi inserido, na posição: | ' if num.count(5) > 0 else '\nO nº 5 não foi inserido.', end='')
        for i, v in enumerate(num):
            if v == 5:
                print(i, end=' | ')
        break
    print()
