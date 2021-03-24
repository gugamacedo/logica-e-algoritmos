# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice

aluno1 = str(input('Aluno 1: '))
aluno2 = str(input('Aluno 2: '))
aluno3 = str(input('Aluno 3: '))
aluno4 = str(input('Aluno 4: '))
num = choice([aluno1, aluno2, aluno3, aluno4])  # [] lista
# random.choice(seq) Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.
print(num)
