# Faça a função ficha() que receba 2 parâmetros opcionais: o nome do jogador e quantos gols marcou. Mesmo que nada tenha sido informado, deverá retornar <desconhecido> ou 0 gol(s)
def ficha(player = '<irineu>', gols = 0):
    return f'{player} fez {gols} gol(s)'


player = str(input('Nome do jogador: ')).title()
gols = str(input('Gols feitos: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if player == '':
    player = '<irineu>'

print(ficha(player, gols))
