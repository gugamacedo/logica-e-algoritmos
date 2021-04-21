# Tenha uma tupla única com nomes de produtos e seus preços na sequência.
# Mostre a listagem de produtos e preços, numa tabela alinhada, de forma tabular
tabela = ('PC', 1199.99, 'Mouse', 9.99, 'Teclado', 29.99, 'Tela', 349.99)
print(f'{"TABELA DE PREÇOS":^40}')
print('-'*40)
# Outro jeito:
# for itens in range(0, len(prod),2):
#     print('{:.<20}R$ {:>6.2f}'.format(prod[itens], prod[itens+1]))
for prod in tabela:
    if type(prod) is str:  # Obrigado, André Maganha! Não conhecia o validador type
        print(f'{prod:.<30}', end='')
    else:
        print(f'R$ {prod:>7.2f}')
print('-' * 40)
