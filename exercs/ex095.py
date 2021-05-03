# Aprimore o exer 93 para que ele funcione para vários jogadores, incluindo um sistema de detalhes do aproveitamento de cada jogador.
team = []
player = {}
gols = []

while True:    
    player['Nome'] = str(input('Digite o nome do jogador: ')).title()
    matches = int(input(f'Quantas partidas {player["Nome"]} jogou? '))
    for c in range(matches):
        gols.append(int(input(f'Quantas gols na {c+1}ª partida: ')))
    player['Gols p/partida'] = gols[:]
    player['Total gols'] = sum(gols)
    team.append(player.copy())
    gols.clear()
    option = str(input('\nQuer cadastrar mais? [S/N] ')).upper()
    while 'S' != option != 'N':
        option = str(input('Quer cadastrar mais? [S/N] ')).upper()
    if option == 'N':
        break

print()
print('Cod ', end='')
for i in player.keys():
    print(f'{i:<15}', end='')
print()
for i, v in enumerate(team):
    print(f'{i+1:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    option2 = int(input('\nQuer ver as partidas de qual jogador [999 pra sair]? '))
    while option2 != 999 and option2 > len(team) or option2 <= 0:
        option2 = int(input('Quer ver as partidas de qual jogador [999 pra sair]? '))
    if option2 == 999:
        print('\nVolte sempre!')
        break
    print(f'\n{team[option2-1]["Nome"]} fez {team[option2-1]["Total gols"]} gol(s)')
    for i, v in enumerate(team[option2-1]["Gols p/partida"]):
        print(f'    => Na partida {i+1} fez {team[option2-1]["Gols p/partida"][i]} gol(s)')
