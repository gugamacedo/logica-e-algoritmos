# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
# in dá um sentido de dentro, == dá um sentido dde valor, precisa usar o []
cidade = str(input('Diga o nome de uma cidade: ')).strip()
# print('SANTO' in cidade.upper().split()[0])  # Tava dando true em SANTOrini ou SANTOs...
print('SANTO' == cidade.upper().split()[0])  # Aqui tá funcionando de boa. Usou 0 == invés de in
# Ele splita, pega o primeiro indice, joga pra maiusculo e verifica se contem SANTO
