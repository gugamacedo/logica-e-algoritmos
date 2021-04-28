# Leia 5 números do user, coloque-os em uma lista, mas os insira ordenados por ordem crescente, e informe a posição
# ao user. nada de sort/sorted! No final exiba a lista
numlist = []
for count in range(0, 5):
    pos = 0
    num = int(input('\nDigite um número: '))
    # Guanabara fez diferente. No meu caso eu optei por verificar se o número inserido é maior que os valores existentes
    # Cada laço for ele anda pela posição, compara com o valor, se for maior ele pega a posição +1 pra ir pra frente do
    # número. Depois disso ele insere, fora do laço, o número na posição que ficou guardada. No inicio do For principal
    # a posição volta ao valor 0, e começa tudo de novo. A solução do prof é muito boa, menor, mas mais complexa
    for i, v in enumerate(numlist):
        if num > v:
            pos = i + 1
    numlist.insert(pos, num)
    if pos == 0:
        print(f'{num} adicionado no começo da lista')
    elif pos > len(numlist)-2:
        print(f'{num} adicionado no final da lista')
    else:
        print(f'{num} adicionado na posição {pos}')
print('\nLista em ordem crescente:', end=' | ')
for nl in numlist:
    print(nl, end=' | ')
