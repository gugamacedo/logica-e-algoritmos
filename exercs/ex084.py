# Leia o NOME E PESO de VARIAS pessoas, guardando tudo em uma matriz.
# Exiba QUANTAS pessoas foram CADASTRADAS, uma LISTAGEM com as pessoas MAIS PESADAS e outra com as MAIS LEVES
persons = []
temp = []
weight = []
while True:
    # -------------------------------------
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    persons.append(temp[:])
    # Valeu, Antônio Evangelista Junior! Não pensei em armazenar em uma lista separada
    weight.append(temp[1])
    temp.clear()
    # -----------------------------------------------------------------
    option = str(input('Cadastrar mais?[S/N]: ')).upper().strip()
    while 'S' != option != 'N':
        option = str(input('Cadastrar mais?[S/N]: ')).upper().strip()
    print()
    if option == 'N':
        break
    # -----------------------------------------------------------------
for p in persons:
    print(f'{p[0]} pesa {p[1]:.2f}', end=' | ')
# Não lembrei do len, tinha usado uma variavel contadoraaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
print(f'\n{len(persons)} pessoas foram cadastradas.')
# -----------------------------------------------------
print(f'O maior peso foi {max(weight):.2f}Kg de ', end='')
for p in persons:
    if p[1] == max(weight):
        print(p[0], end='...')
print(f'\nO menor peso foi {min(weight):.2f}Kg de ', end='')
for p in persons:
    if p[1] == min(weight):
        print(p[0], end='...')
