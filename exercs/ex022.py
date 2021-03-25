'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.

'''
nometd = str(input('Digite seu nome completo: ')).strip()
print(nometd.upper())
print(nometd.lower())
# print(f'Seu nome tem ao toodo {len(nometd) - nometd.count(" ")} letras')
print(f'Seu nome completo tem {len(nometd.replace(" ", ""))} letras')
print(f'Seu primeiro nome é {nometd.split()[0][0:]}')
print(f'Seu sobrenome é {nometd.split()[-1][0:]}')
print(f'Seu primeiro nome tem {len(nometd.split()[0][0:])} letras')
# print(f'Seu primeiro nome tem {nometd.find(" ")} letras')
