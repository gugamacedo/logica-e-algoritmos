# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média
nota1 = float(input('Diz a nota da P1: '))
nota2 = float(input('Diz a nota da P2: '))
nota3 = float(input('Diz a nota da NT: '))
notatot = nota1+nota2+nota3
print(f'A média do aluno é {notatot/3:.2f}')
