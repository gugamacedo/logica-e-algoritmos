# Leia o NOME, IDADE, e GÊNERO de 4 PESSOAS. No final, mostre:
# a MÉDIA DE IDADE do grupo; qual o NOME do HOMEM MAIS VELHO; QUANTAS MULHERES tem MENOS DE 20 anos
med_age = 0
age_man = 0
name_man = ''
qtwomen = 0

for count in range(1, 5):
    name = str(input(f'Nome da {count}ª pessoa: '))
    age = int(input(f'Idade da {count}ª pessoa: '))
    gen = str(input(f'Gênero (H/M) da {count}ª pessoa: ')).upper()
    print('-'*20)

    med_age += age
    if age > age_man and gen == 'H':
        age_man = age
        name_man = name
    elif age < 20 and gen == 'M':
        qtwomen += 1

print(f'A média de idade do grupo é {med_age/4} anos.\n'
      f'O homem mais velho se chama {name_man} e tem {age_man} anos.\n'
      f'Tem {qtwomen} mulheres com menos de 20 anos.')
