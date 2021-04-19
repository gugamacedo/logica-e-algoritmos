# Mostre a tabudada de algum número soliticatado, várias vezes, até o user digitar algum valor negativo
while True:
    num = int(input('\nQual número você quer a tabuada? '))
    if num <= 0:
        break
    for count in range(1, 11):
        print(f'{num} * {count} = {num*count}')
print('Acabou')
