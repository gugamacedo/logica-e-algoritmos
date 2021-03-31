'''Crie um programa que leia 2 notas de um aluno e calcule se passou ou não, ou está de recuperação e exiba o resultado
abaixo de 5 reprovado, entre 5 e 7 recuperação, acima de 7 passou'''
grade1 = float(input('Digite a 1ª nota: '))
grade2 = float(input('Digite a 2ª nota: '))
average = (grade1 + grade2) / 2
print(f'Sua média é {average:.2f}')
if average < 5:
    print('Você está reprovado, se fuuuu')
elif 5 <= average < 7:
    print('Quaaaase, está em recuperação, dá pra se salvar!')
else:
    print('2 palavras pra você: PARA BÉNS')
