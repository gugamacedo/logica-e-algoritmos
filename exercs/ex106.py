# faça um mini-sistema que otilize o interactive help. O usuário vai digitar a fução/lib e o manual vai aparecer. Acaba quando digitar 'fim'. Utilize cores
# não tive paciência pra ficar colorindo 🥱😴

def ajuda(metodo):
    help(metodo)


print('~'*10)
print(f'{"PyHelp":^10}')
print('~'*10)

while True:
    metodo = str(input('\nQual função/lib quer ver? ["stop" para sair] '))
    if metodo.lower() == 'stop':
        break
    elif metodo != '':
        ajuda(metodo) 
