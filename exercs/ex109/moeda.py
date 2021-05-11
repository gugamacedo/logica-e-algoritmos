def aumentar(valor, formatar):
    valor *= 1.10 
    return valor if formatar == False else moeda(valor)

def diminuir(valor, formatar):
    valor *= 0.90 
    return valor if formatar == False else moeda(valor)

def dobrar(valor, formatar):
    valor *= 2
    return valor if formatar == False else moeda(valor)

def metade(valor, formatar):
    valor *= 0.5
    return valor if formatar == False else moeda(valor)

def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')
