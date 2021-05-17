# Reescreva a função leia_int() incluindo a possibilidade da digitação de um número inválido. 
# Também crie a função leia_float() com a mesma funcionalidade

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


def leia_float(valor):
    while True:
        try:
            num = float(input((valor)))
        except (ValueError, TypeError):
            print(f'\033[31mErro!\033[m Tipo de dado errado!')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mErro!\033[m Dados não informados!')
            return 0
        else:
            return num

num1 = leia_int('Digite um número inteiro: ')
num2 = leia_float('Digite um número float: ')
print(f'O número inteiro foi {num1}')
print(f'O número float foi {num2}')
