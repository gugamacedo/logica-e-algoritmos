# Leia vários números, pergunte se o user deseja inserir mais,
# e exiba quantos nº foram inseridos, a média entre eles, o menor e maior valor
ok = 'S'
num = count = numstock = numbig = numsmall = 0
while ok != 'N':
    if ok == 'S':
        num = int(input('Digite um número: '))
        count += 1
        numstock += num
        if count == 1:
            numsmall = num
            numbig = num
        if num > numbig:
            numbig = num
        elif num < numbig:
            numsmall = num
        ok = str(input('Deseja inserir mais números? [S/N]: ')).upper().replace(' ', '')
    elif 'N' != ok != 'S':
        ok = str(input('Opção inválida! Deseja inserir mais números? [S/N]: ')).upper().replace(' ', '')
print(f'\nVocê digitou {count} números.\nA média entre eles foi {numstock/count}.\n'
      f'O maior número é o {numbig} e o menor é {numsmall}.')
