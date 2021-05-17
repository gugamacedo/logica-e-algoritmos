def leia_int(valor):
    while True:
        try:
            num = int(input((valor)))
        except (ValueError, TypeError):
            print(f'\033[31mErro!\033[m Tipo de dado errado!')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mErro!\033[m Dados não informados!')
            return 0
        else:
            return num

def linha(tam=40):
    return '-'*tam

def mensagem(msg):
    print(linha())
    print(msg.center(40))
    print(linha())

def options(lista):
    mensagem('OPÇÕES')
    for i,v in enumerate(lista):
        print(f'{i+1} - {v}')
    print(linha())
    opt = leia_int('Escolha uma opção: ')
    return opt
