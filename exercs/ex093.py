# Leia o nome do jogador e quantas partidas ele jogou. Depois leia a quantidade de gols em cada partida e guarde numa lista dentro do dicionário. Guarde tudo em um dicionário, incluindo o total de gols feitos.
player = {}
gols = []

player['Nome'] = str(input('Digite o nome do jogador: ')).title()
matches = int(input(f'Quantas partidas {player["Nome"]} jogou? '))
for c in range(matches):
    gols.append(int(input(f'Quantas gols na {c+1}ª partida: ')))
player['Gols p/partida'] = gols[:]
player['Total gols'] = sum(gols)

print()
print(f'{player["Nome"]} jogou {matches} partida(s)')
for i, v in enumerate(player["Gols p/partida"]):
    print(f'    => Na partida {i+1} fez {v} gol(s)')
print(f'=> Total de {player["Total gols"]} gol(s)' if player["Total gols"] > 0 else '=> Fez poha nenhuma, demitido!')
