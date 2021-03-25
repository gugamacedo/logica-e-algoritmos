# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Diga seu nome inteiro: ')).strip()
# in dá um sentido de dentro, == dá um sentido dde valor, precisa usar o []
# print('SILVA' in nome.upper())  # Tava dando true em SILVAna ou SILVAnei...
print('SILVA' in nome.upper().split())  # Converto o nome para letras maiúsculas, depois o divido
