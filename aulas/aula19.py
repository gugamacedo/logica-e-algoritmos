'''
Dicionários {}

Similar a lista, mas tem a estrutura é key: value, além de itens. 

filme = {
    'titulo': 'Star Wars',
    'ano': 1997,
    'diretor': 'Jorge Lucas'
}

print(filme.keys())
print(filme.values())
print(filme.items())

# aqui o for percorre as keys e values dos os itens do dicionário filme
for k, v in filme.items():
    print(f'O {k} é {v}.')

locadora = [{
    'titulo': 'Matrix',
    'ano': 1999,
    'diretor': 'Wachowski'
}]

print(locadora)
locadora.append(filme)
print(locadora)
print(locadora[0]['titulo'])    
dados = {
    'nome': 'Pedro',
    'idade': 25
}


print(dados)
print(f'{dados["nome"]} tem {dados["idade"]} anos.')
dados['idade'] = 26
print(dados)
# no caso do dicionário, pra adicionar item você não usa .append
dados['genero'] = 'H' # se a key não existe, ela é criado
print(dados)
#remover key
del dados['idade']
print(dados)

brasil = []
estado1 = {
    'uf': 'São Paulo',
    'sigla': 'SP'
}
estado2 = {
    'uf': 'Rio de Janeiro',
    'sigla': 'RJ'
}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])

brasil = []
estado = {}

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).title()
    estado['sigla'] = str(input('Sigla: ')).upper()
    # brasil.append(estado[:])          
    # Lembra que em lista, no append usamos [:] pra representar umaa cópia independente? Pra adicionar um dicionário cópia independente, isso é representado pelo método .copy()
    brasil.append(estado.copy())

for estado in brasil: # esse é o for da lista
    for v in estado.values(): # for do dicionário
        print(v, end=' | ')
    print()

https://www.alura.com.br/artigos/trabalhando-com-o-dicionario-no-python
'''
