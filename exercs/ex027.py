# Faça um programa que leia o nome completo de uma pessoa,mostrando em seguida o primeiro e o último nome separadamente.
nometd = str(input('Digite seu nome completo: ')).strip()
print(f'Olá {nometd.title().split()[0][0:]} {nometd.title().split()[-1][0:]}\n'
      f'Olá {nometd.title().split()[0][0:]}\n'
      f'Olá {nometd.title().split()[-1][0:]}')
