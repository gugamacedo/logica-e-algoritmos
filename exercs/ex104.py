# faça a função leia_int() que funcionará como um input, mas que só aceita Int
def leia_int(texto):
    while True:
        num = str(input((texto))).replace(' ', '')
        if num.isnumeric():
            num = int(num)
            return num
        else:
            print('\033[31mErro!\033[m')


num = leia_int('Digite um número inteiro: ')
print(f'O número inserido foi {num}')
