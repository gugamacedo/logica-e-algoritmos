# Escolha par ou ímpar, jogue um número, some com o pc e vê quem acertou. O jogo será interrompido quando o user perder
from random import randint
from time import sleep
countwin = 0
while True:
    useroption = str(input('Escolha Par ou Ímpar [I/P]: ')).upper()
    while 'P' != useroption != 'I':
        useroption = str(input('Escolha Par ou Ímpar [I/P]: ')).upper()
    usernum = int(input('Escolha um número: '))
    pcnum = randint(0, 10)
    print(f'PC escolheu {pcnum}')
    print('\nCalculando resultado...')
    sleep(1)
    result = usernum+pcnum
    if result % 2 == 0 and useroption == 'P':
        print(f'\033[1;32mVocê ganhou, deu Par, a soma foi {result}.\n')
        countwin += 1
    elif result % 2 != 0 and useroption == 'I':
        print(f'\033[1;32mVocê ganhou, deu Ímpar, a soma foi {result}.\n')
        countwin += 1
    elif result % 2 == 0 and useroption == 'I':
        print(f'\033[1;31mPC ganhou, deu Par, a soma foi {result}.')
        print(f'\033[1;32mVocê ganhou {countwin} vezes seguidas.' if countwin > 0 else'', end='')
        break
    elif result % 2 != 0 and useroption == 'P':
        print(f'\033[1;31mPC ganhou, deu Ímpar, a soma foi {result}.')
        print(f'\033[1;32mVocê ganhou {countwin} vezes seguidas.' if countwin > 0 else'', end='')
        break
