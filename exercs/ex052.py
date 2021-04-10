# Leia um número inteiro e diga se ele é ou não primo. Números primos são divisiveis apenas por 1 e ele mesmo
nump = int(input('Digite um número e descubra se ele é primo: '))
stock = 0

for c in range(1, nump+1):  # +1 porque sempre vai um a menos
    # print(nump % c == 0)  Exibindo o contador de true or false
    if nump % c == 0:
        stock += 1  # conforme da True, ele armazena 1

if stock == 2:  # aqui ele verifica pois numeros primos são apenas divisiveis 2 vezes
    print(f'Foi divisível {stock} vezes...então é primo!')
else:
    print(f'Foi divisível {stock} vezes...então não é primo!')
