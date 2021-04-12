# Leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas atingiram a maioria e quantas não são
from datetime import date

stock = 0
for count in range(1, 8):
    yearsys = date.today().year
    yearbirth = int(input(f'Em qual ano a {count}ª pessoa nasceu? '))
    # Também dá pra simplificar assim:   age = date.today().year - int(input('Qual seu ano de nascimento? '))
    age = yearsys - yearbirth
    if age >= 18:
        stock += 1

print(f'{stock} pessoas são maiores de idade!')
if stock != 7:
    print(f'{7 - stock} pessoas são menores de idade!')
