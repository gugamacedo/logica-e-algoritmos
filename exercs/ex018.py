# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan

ang = int(input('Qual o ângulo que quer calcular? '))
newang = radians(ang)
# Aqui em NEWANG você teve que converter graus para radianos,
# pois seno e cosseno se calcula em radianos
print(f'O seno do ângulo {ang}∘ é {round(sin(newang), 2)}\n'
      f'O cosseno do ângulo {ang}∘ é {round(cos(newang), 2)}\n'
      f'A tangente do ângulo {ang}∘ é {round(tan(newang), 2)}')
