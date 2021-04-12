# Leia o peso de 5 pessoas e diga qual o maior e menor peso
weightbig = 0
weightsmall = 0
for counting in range(1, 6):
    newweight = float(input(f'Qual o peso da {counting}ª pessoa? '))
    if counting == 1:
        weightbig = newweight
        weightsmall = newweight
    else:
        if newweight > weightbig:
            weightbig = newweight
        elif newweight < weightsmall:
            weightsmall = newweight
# Dá pra cortar tdo esse proceso usando oas funções max e min, mas o objtivo aqui é usar o for e if
print(f'O maior peso é {weightbig}Kg.\nO menor peso é {weightsmall}Kg')
