# Escreva um program que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$1250 calcule um aumento de 10%. Para inferiores 15%
salar = float(input('Quanto você ganha por mês? R$'))
if salar >= 1250:
    print(f'Okay, seu aumento será de R${salar * 0.10:.2f}\n'
          f'Seu novo salário é R${salar * 1.10:.2f} uhuuuuuul')
# dá pra colocar o 1.00 pra multiplicar junto com o próprio valor, sem precisar somar
else:
    print(f'Okay, seu aumento será de R${salar * 0.15:.2f}\n'
          f'Seu novo salário é R${salar * 1.15:.2f} uhuuuuuul')
