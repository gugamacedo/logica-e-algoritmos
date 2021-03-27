# Faça um program que leia um ano qualquer e diga se é bissexto ou não
from datetime import date  # Para achar a data atual
ano = int(input('Descubra qual ano é ou não bissexto: \nDigite 0 se for ano atual: '))
# if ano % 4 == 0: Tá errado, exceto anos múltiplos de 100 que não são múltiplos de 400
if ano == 0:
    ano = date.today().year  # dá pra mudar uma variavel de acordo com a condicional, muito útil!!
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
