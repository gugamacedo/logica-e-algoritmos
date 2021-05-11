# Arrume a formatação na saida, para dinheiro, do exer 107
import moeda

valor = float(input('Digite um valor: R$'))

print()
print(f'Aumentando 10% o valor {moeda.moeda(valor)} -> {moeda.moeda(moeda.aumentar(valor))} ')
print(f'Diminuindo 10% o valor {moeda.moeda(valor)} -> {moeda.moeda(moeda.diminuir(valor))} ')
print(f'O dobro do valor {moeda.moeda(valor)} -> {moeda.moeda(moeda.dobrar(valor))} ')
print(f'A metade do valor {moeda.moeda(valor)} -> {moeda.moeda(moeda.metade(valor))} ')
