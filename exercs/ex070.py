''' Cadastro de produtos: leia o nome e preço de várias produtos. Depois pergunte se quer continuar cadastrando,
se quiser faça o mesmo processo. Quando não qusier mais, mostre:
total das compras, quantas produtos custam mais de 1K, e o nome e preço do produto mais barato '''
totprice = countprod = count = lowprod = 0
prodnmlow = ''
while True:
    prodname = str(input('\nDigite o nome do produto: ')).capitalize().strip()
    price = input('Digite o preço do produto: R$')
    while str(price.isnumeric()) != 'True':
        price = input('Digite o preço do produto: R$')
    price = float(price)
    totprice += price
    if price > 1000:
        countprod += 1
    count += 1
    if count == 1:
        lowprod = price
        prodnmlow = prodname
    if price < lowprod:
        lowprod = price
        prodnmlow = prodname
    option = str(input('\nQuer continuar? [S/N] ')).upper().strip()
    while 'S' != option != 'N':
        option = str(input('Quer continuar? [S/N] ')).upper().strip()
    if option == 'N':
        print(f'\nVocê gastou no total R$ {totprice:.2f}.\n{countprod} produtos custam mais de R$1000.00'
              f'\nO produto mais barato foi {prodnmlow}, que custou R${lowprod:.2f}')
        break
