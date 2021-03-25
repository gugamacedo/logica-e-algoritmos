'''
# Quando quiser mostrar texto longo, 3 aspas simples no começo e final

# fatiamento de string 05:12
frase = 'pythonic way'
print(frase[9])  # lembre-se, o primeiro número é 0
print(frase[0])  # Para mostrar o primeiro indice
print(frase[-1])  # Para mostrar o último indice
print(frase[9:12])  # ele descarta o último caractere, então tem que ir 1 a frente do que quer
print(frase[0:12:2])  # o 1º e 2º parâmetro é onde começa e onde termina. O 3º é quantos caracteres vai "pular"
print(frase[:5])  # quando você omite o 1º parâmetro, ele assume como 0. Vai do 0 ao 5, também eliminando o 5
print(frase[9:])  # mesmo caso que acima, mas omitindo o 2º parâmetro. Aqui ele começa do 9 e vai até o final
print(frase[9::2])  # aqui o 1º parâmetro diz onde começa, e no 2º parâmetro diz quantas casas pular

# 13:50 - Análise de string
frase = 'pythonic way'
len(frase)  # comprimento, quantos caracteres tem a frase
frase.count('0')  # count conta tal coisa dentro da frase, no caso o 'o'
frase.count('o', 0, 12)  # aqui count junto com fatiamento, onde começa a contar e onde termina
frase.find('way')  # indica onde começa certa parte procurada. Se não houver o procurado, retorna -1
'way' in frase  # Diz se tem ou não o que procura dentro da string, retorna true or false

# 19:35 - Transformação
frase = 'pythonic way'
String é imutável, ah não ser que substitua e salve a mudança da string, para isso tem que usar frase = frase.metódo
frase.replace('pythonic way', 'pythonic')  # Substitui algo dentro da string
frase.upper()  # Deixa tudo em maiusculo
frase.lower()  # Deixa tudo em minusculo
frase.capitalize()  # Deixa a 1ª letra da 1ª palavra da frase em maiusculo e o resto em minusculo
frase.title()  # Deixa a 1ª letra de cada palavra da frase em maiusculo e o resto em minusculo,
# O title consegue fazer isso através de uma análise dos espaços, o que estiver entre espaços conta como palavra
frase.strip()  # remove os caracteres de espaços no começo e final da string
frase.rstrip()  # remove os caracteres de espaços da direita, do final da string
frase.lstrip()  # remove os caracteres de espaços da esquerda, do começo da string

# 26:35 - Divisão
frase = 'pythonic way'
frase.split()  # divide a string em várias palavras numa lista que recebem indexação nova, cada uma começa docaractere 0
' '.join(frase)  # junta tudo para uma string inteira. No começo você define o que fica entre as divisões

frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:14])
print(frase[:14])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print(frase.upper().count('O'))  # dá para juntar métodos
print(len(frase.strip()))
print(frase.replace('Python', 'Rust'))
print(frase.replace('o', 'a'))
frase = frase.replace('Python', 'Rust')
print(frase)
frase = frase.replace('Rust', 'Python')
print(frase)
frase = frase.split()
print(frase)
print(frase[0])
print(frase[0][2])  # Mostra primeiro index, 2 caractere
print(frase.split()[0][0:]} {frase.split()[-1][0:])
print(frase.split()[0][0:]})
print(frase.split()[-1][0:]})
frase = ' '.join(frase)
print(frase)
'''