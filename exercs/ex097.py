# Faça uma função chamada escreva() que recebe um texto qualquer como parâmetro e mostre com as linhas adaptaveis
# 2 left 2 right
def escreva(message):
    width = len(message)+4
    print('~'*width)
    print(f'{message:^{width}}')
    print('~'*width)


message = str(input('Escreva um título: ')).title()
escreva(message)