# Uma matriz com 3 niveis. Leia o nome, duas notas e a média de vários alunos e guarde cada em uma lista dentro de outa lista. No final, mostre o boletim contendo a média de cada um e permita que o user possa mostrar as notas de cada um individualmente

# Você quebrou a cabeça nesse porque queria fazer com For. O For só pode ser usado se você tem um limitador PRÉ DEFINIDO, não pode alterar o limitador, é fixo e pré estabelicido. No caso desse exer, tem que ser While

matrix = []
print('Cadastre o primeiro aluno: ')

while True:
    name = str(input('Nome: '))
    n1 = float(input('1ª nota: '))
    n2 = float(input('2ª nota: '))
    average = round((n1 + n2) / 2, 2)
    matrix.append([name, [n1, n2], average])
    # print(matrix)
    option = str(input('\nCadastrar mais [S/N]? ')).upper()
    while 'S' != option != 'N':
        option = str(input('Cadastrar mais [S/N]? ')).upper()
    if option == 'N':
        print()
        print('-=-'*7)
        print('  Boletim escolar')
        print('-=-'*7)
        print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}') # FOrmatação interessante...
        for i, v in enumerate(matrix):
            print(f'{i+1:<4}{v[0]:<10}{v[2]:>8.2f}')
        while True:
            option2 = int(input('\nQuer ver as notas de qual aluno [999 pra sair]? '))
            if option2 == 999:
                break
            print(f'As notas de {matrix[option2-1][0]} são {matrix[option2-1][1][0]} e {matrix[option2-1][1][1]}')
        break
