# Faça um algoritmo que leiao preço de um produto e mostre seu novo preço, com 5% de desconto
prod = float(input('Preço do produto: '))
print(f'Com o desconto, o produto custará R${prod * 1.05:.2f}\n'
      f'(O desconto dado foi R${prod * 0.05:.2f})')
