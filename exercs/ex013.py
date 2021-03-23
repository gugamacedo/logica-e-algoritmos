# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salr = float(input('Qual seu salário? '))
print(f'Parabéns, você ganhou um aumento! Seu novo salário é R${salr * 1.15:.2f}\n'
      f'(O aumento dado foi de R${salr * 0.15:.2f})')
