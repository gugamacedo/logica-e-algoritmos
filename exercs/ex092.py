# Leia nome, ano de nascimento (como idade) e carteira de trabalho e cadastre-os em um dicionário. Se CTPS diferente de zero, o dicionário perguntará também o ano de contratação e o salário. Calcule e acrescente com quantos anos a pessoa vai se aposentar (35 anos após contratação.)
from datetime import date

person = {}
person['Nome'] = str(input('Digite seu nome: ')).title()
person['Idade'] = date.today().year - int(input('Digite seu ano de nascimento: '))
person['Carteira de Trabalho'] = int(input('Digite sua Carteira de Trabalho [0 se não tiver]: '))
if person['Carteira de Trabalho'] != 0:
    person['Ano de Contratação'] = int(input('Digite o ano de contratação: '))
    person['Salário'] = float(input('Digite o salário: '))
    person['Idade Aposentadoria'] = (person['Ano de Contratação'] + 35) - (date.today().year - person['Idade'])
else:
    del person['Carteira de Trabalho']

print()
for k, v in person.items():
    print(f'{k}: {v}')
