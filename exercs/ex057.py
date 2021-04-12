# Leia o genêro de uma pessoa, mas só aceite os valores H ou M. Caso esteja errado, pea que digite novamente.
gen = str(input('Digite seu genêro (M ou H): ')).upper().strip()
while 'M' != gen != 'H':
    # while gen not in 'MH':    O guanabara fez assim mas dá errado pois aceita "mh" ou "hm"
    print('Inválido\n')
    gen = str(input('Digite seu genêro (M ou H): ')).upper()
if gen == 'M':
    print('Tu é muié então...')
elif gen == 'H':
    print('Tu é homi então...')
