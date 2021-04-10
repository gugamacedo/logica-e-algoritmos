# Leia uma frase, diga se ela é um palíndromo, desconsiderando espaços (de trás pra frente)
phrase = str(input('Digite alguma frase/palavra qualquer: ')).lower().replace(' ', '')
if phrase == phrase[::-1]:
    print('Palíndrimo')
else:
    print('Não dá')
