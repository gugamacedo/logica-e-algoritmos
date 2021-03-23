# Faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
altr = float(input('Altura da parede em metros: '))
larg = float(input('Largura da parede em metros: '))
area = altr*larg
print(f'A área da sua parede é {area}m²\n'
      f'Você vai precisar de {area / 2} litros de tinta')