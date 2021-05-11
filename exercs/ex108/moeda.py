def aumentar(valor):
    valor *= 1.10 
    return valor

def diminuir(valor):
    valor *= 0.90 
    return valor

def dobrar(valor):
    valor *= 2
    return valor

def metade(valor):
    valor *= 0.5
    return valor

def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')
