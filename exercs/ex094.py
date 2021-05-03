# Leia nome, gênero e idade de várias pessoas, guardando cada uma em um dicionário. Coloque todos dentro de uma lista. No final mostre: quantas pessoas foram cadastradas; a média de idade do grupo; uma lista com todas mulheres; uma lista com todos as pessoas com idade acima da média
group = []
person = {}
stock_age = 0

while True:
    person['Nome'] = str(input('Digite seu nome: ')).title()
    person['Gênero'] = str(input('Digite seu gênero [M/H]: ')).upper()
    while 'M' != person['Gênero'] != 'H':
        person['Gênero'] = str(input('Digite seu gênero [M/H]: ')).upper()
    person['Idade'] = int(input('Digite sua idade: '))        
    group.append(person.copy())

    option = str(input('\nQuer cadastrar mais? [S/N] ')).upper()
    while 'S' != option != 'N':
        option = str(input('Quer cadastrar mais? [S/N] ')).upper()
    if option == 'N':
        break

for p in group:
    stock_age += p['Idade'] / len(group)

print(f'\nO grupo tem {len(group)} pessoas\nA média de idade do grupo é {round(stock_age, 2)} anos')

print(f'As mulheres são: ', end='')
for p in group:
    if p['Gênero'] == 'M':
        print(p['Nome'], end=' | ') 

print(f'\nAs pessoas com idade acima da média são: ', end='')
for p in group:
    if p['Idade'] > stock_age:
        print(p['Nome'], end=' | ') 