# Faça um programa que leia o comprimento do cateto oposto a do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comrpimento da hipotenusa.
from math import hypot

alt = float(input('Qual a altura do triângulo? '))  # cateto oposto
base = float(input('Qual a base? '))  # cateto adjacente
# Existe 2 formas, a matemática manual, ou com o método da biblioteca
# hipo = alt**2+base**2
# print(f'A hipotenusa mede {round(hipo**0.5, 2)}')
hipo = hypot(alt, base)
print(f'A hipotenusa mede {round(hipo, 2)}')
