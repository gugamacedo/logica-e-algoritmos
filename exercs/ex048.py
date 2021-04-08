# Calcule a soma entre todos números ímpares múltiplos de 3, entre 1 e 500
stock = 0
for count in range(1, 501):
    # Também pode fazer range(1, 501, 2) ou range(3, 501, 3). E tirar metade do IF abaixo
    if count % 2 != 0 and count % 3 == 0:
        stock += count
        print(f'{count} - {stock}')
print(f'\n{stock}')
