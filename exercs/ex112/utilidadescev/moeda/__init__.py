def aumentar(valor, taxa):
    valor *= (1+taxa/100) 
    return moeda(valor)

def diminuir(valor, taxa):
    valor *= (1-taxa/100) 
    return moeda(valor)

def dobrar(valor):
    valor *= 2
    return moeda(valor)

def metade(valor):
    valor *= 0.5
    return moeda(valor)

def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')

def resumo(valor, taxamais, taxamenos):
    print()
    print('-'*32)
    print(f'{"RESUMO DO VALOR":^32}')
    print('-'*32)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobrando preço: \t{dobrar(valor)}')
    print(f'Metade do preço: \t{metade(valor)}')
    print(f'Aumentando preço {taxamais}%: \t{aumentar(valor, taxamais)}')
    print(f'Diminuindo preço {taxamenos}%: \t{diminuir(valor, taxamenos)}')
