# Mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com pausa de 1 segundo
from time import sleep
import emoji
for counting in range(10, -1, -1):
    print('...', counting)
    sleep(0.6)
print(emoji.emojize(':collision::tada:'*10, use_aliases=True))
