# Mostre os 5 primeiros times, Os últimos 4 times, Em ordem alfabética, E a posição do Mengão
tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athlético Paranaense', 'São Paulo', 'Internacional',
          'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Athlético Mineiro', 'Fluminense',
          'Botafogo', 'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')

print('-'*50)
for times in tabela[:5]:
    print(f'{tabela.index(times)+1}º colocado - {times}')

print('-'*50)
for times in tabela[-4:]:
    print(f'{tabela.index(times)+1}º colocado - {times}')

print('-'*50)
print(f'Mengão está em {tabela.index("Flamengo")+1}º colocado no Brasileirão')

print('-'*50)
for times in sorted(tabela):
    print(f'{times}')
