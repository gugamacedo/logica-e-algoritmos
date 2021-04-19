# Mesma coisa do 64 mas com o uso do break no 999
numstock = count = 0
while True:
    num = int(input('\n[999 encerra o app] \nDigite um número: '))
    if num == 999:
        break
    numstock += num
    count += 1
print(f'\nVocê digitou {count} números.\nA soma entre eles deu {numstock}')
