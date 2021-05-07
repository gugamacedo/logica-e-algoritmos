# Faça uma função chamada area(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostra a area do terreno
def area(width, length):
    area = width*length/2
    print(f'A área é {area}m²') 


width = float(input('Digite a largura (m): '))
length = float(input('Digite o comprimento (m): '))
area(width, length)
