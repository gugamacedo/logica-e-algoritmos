# Leia o primeiro termo e a razão de uma Progressão Aritmética. No final mostre os 10 primeiros termos da PA
# Razão é a constante, a fórmula pra pular de num em num
print('10 termos de uma PA\n')
firsterm = int(input('Digite o 1º termo da Progressão aritmética: '))
reason = int(input('Digite a constante da PA: '))
for count in range(firsterm, firsterm+10):
    print(firsterm)
    firsterm += reason
