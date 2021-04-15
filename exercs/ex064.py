# Leia vários números inteiros, mostre quantos foram digitados e a soma entre eles.
# Use o número 999 pra parar o programa e desconsidere-o na soma
num = numstock = count = 0
while num != 999:
    num = int(input('\n[999 encerra o app] \nDigite um número: '))
    numstock += num
    count += 1
print(f'\nVocê digitou {count-1} números.\nA soma entre eles deu {numstock-999}')
