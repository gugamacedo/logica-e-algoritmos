# Faça o computador jogar Jokenpô com você
from random import randint
from time import sleep
import emoji

mejoken = int(input('1)     Pedra\n'
                    '2)     Papel\n'
                    '3)     Tesoura\n'
                    'Selecione o número do que quer jogar: '))
itens = ('', ':fist:', ':hand:', ':v:')  # lista de vetores, assim fica mais fácil do sair delcarar cada número
pcjoken = randint(1, 3)

'''
if pcjoken == 1:
    pcjoken = 'Pedra'
elif pcjoken == 2:
    pcjoken = 'Papel'
else:
    pcjoken = 'Tesoura'

if mejoken == 1:
    mejoken = 'Pedra'
elif mejoken == 2:
    mejoken = 'Papel'
elif mejoken == 3:
    mejoken = 'Tesoura'
else:
    print('Número inválido')
'''
if 1 <= mejoken <= 3:
    print('\nJoken...')
    sleep(1)
    print('...pô!')
    print('-=====' * 5)

    if mejoken == 1 and pcjoken == 2 or mejoken == 3 and pcjoken == 1 or mejoken == 2 and pcjoken == 3:
        print(emoji.emojize(f'\nVocê: \033[1;31m{itens[mejoken]}\033[m\nPC: \033[1;32m{itens[pcjoken]}\n'
                            f'\033[1;31mPC ganhouu!', use_aliases=True))
    elif mejoken == 2 and pcjoken == 1 or mejoken == 1 and pcjoken == 3 or mejoken == 3 and pcjoken == 2:
        print(emoji.emojize(f'\nVocê: \033[1;32m{itens[mejoken]}\033[m\nPC: \033[1;31m{itens[pcjoken]}\n'
                            f'\033[1;32mVocê ganhouu!', use_aliases=True))
    else:
        print(emoji.emojize(f'\nVocê: \033[1;33m{itens[mejoken]}\033[m\nPC: \033[1;33m{itens[pcjoken]}\033[m\n'
                            f'\033[1;33mEmpatouuu!', use_aliases=True))
else:
    print('Opção inválida!')
