# Fazer uma lista de palavras aleatórias sem acentos, e mostrar quais vogais tem em cada uma
words = ('RFG', 'Flamengo', 'Santos', 'Palmeiras', 'Internacional', 'Corinthians', 'Fortaleza',
         'Bahia', 'Vasco da Gama', 'Fluminense', 'Botafogo', 'Cruzeiro', 'Csa', 'Chapecoense')
for w in words:  # o primeiro for analisa cada palavra dentro da tupla
    print(f'\n{w} tem as vogais: ', end='')
    for vocalic in w:  # o segundo for analisa cada letra dentro de cada palavra
        if vocalic.lower() in 'aeiou':
            print(vocalic, end=' ')
