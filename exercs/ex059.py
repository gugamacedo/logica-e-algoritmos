# Leia 2 valores e mostre um menu na tela. Seu programa deverá relizar a ação solicitada em cada caso
# 1-Somar 2-Multiplicar 3-Maior 4-Novos números 5-Sair do programa
num1 = int(input('Insira o 1º valor: '))
num2 = int(input('Agora insira o 2º valor: '))
option = 0
while option != 5:
    print('\nMenu\n1-Somar\n2-Multiplicar\n3-Maior número\n4-Novos números\n5-Sair do programa')
    option = int(input('Escolha um opção: '))
    if option == 1:
        print(num1+num2)
    elif option == 2:
        print(num1*num2)
    elif option == 3:
        if num1 > num2:
            print(f'O número {num1} é o maior!')
        elif num2 > num1:
            print(f'O número {num2} é o maior!')
        else:
            print('Ambos números são iguais')
    elif option == 4:
        print()
        num1 = int(input('Insira o novo 1º valor: '))
        num2 = int(input('Agora insira o novo 2º valor: '))
    elif 1 > option > 5:
        print('Opção inválida')
print('\nPrograma encerrado!')
