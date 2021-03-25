# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite alguma coisa qualquer: ')).strip()
print(f'A letra A aparece {frase.upper().count("A")} vezes'
      f'Aparece pela 1ª vez no caractere {frase.upper().find("A")}'
      f'Aparece pela última vez no caractere {frase.upper().rfind("A")}')
# Coloquei o r em find para indicar right, mandar ele deve achar a 1ª ocorrência pela direita, ao contrário
# Sem o r ele vai naturalmente pela esquerda, porque assume a contagem dos caracteres, que começa pelo 0
