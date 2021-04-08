# Mostre na tela todos os números pares entre 1 e 50
for counting in range(1, 51):
    # Também pode fazer range(2, 51, 2). E tirando o IF. Ocuparia menos processamento pois já saí pulando
    if counting % 2 == 0:
        print(counting, end=' - ')
