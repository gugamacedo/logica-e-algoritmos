# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

aluno1 = str(input('Aluno 1: '))
aluno2 = str(input('Aluno 2: '))
aluno3 = str(input('Aluno 3: '))
aluno4 = str(input('Aluno 4: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
# random.shuffle(x[, random])
# Shuffle Embaralha the sequence x in place.
# Apenas embaralha, por padrão não retorna nada
print(alunos)
