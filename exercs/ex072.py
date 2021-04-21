# Tenha uma tupla totalmente preenchida com uam contagem por extenso, de zero à vinte
# Seu programa deverá ler o número digitado pelo user e mostrá-lo pro extenso, deesde que esteja no range
num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numuser = int(input('Digite um nº entre 0 e 20: '))
    if 20 >= numuser >= 0:
        print(f'Número {num[numuser]}.')
        option = str(input('Quer continuar? [S/N]: ')).upper()
        while 'S' != option != 'N':
            option = str(input('Quer continuar? [S/N]: ')).upper()
        if option == 'N':
            break
        print()
