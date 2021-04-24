num = []
nummax = []
nummin = []
for count in range(0, 5):
    num.append(int(input(f'Digite um número na posição {count}: ')))  # pode usar o for pra repetir o input na lista
print(f'\nVocê inseriu os números', end=' ')
for nn in num:
    print(nn, end=' ')
for pos, n in enumerate(num):
    if n == max(num):
        nummax.append(pos)
    if n == min(num):
        nummin.append(pos)
print(f'\nO maior número é o {max(num)} e está na posição', end=' | ')
for nmax in nummax:
    print(nmax, end=' | ')
print(f'\nO menor número é o {min(num)} e está na posição', end=' | ')
for nmin in nummin:
    print(nmin, end=' | ')
