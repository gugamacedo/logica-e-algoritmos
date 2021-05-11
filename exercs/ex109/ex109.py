# Modifique as funções moeda.py, para que aceite um parametro amais, informando se o valor será ou não formato para dinheiro
import moeda

valor = float(input('Digite um valor: R$'))

print()
print(f'Aumentando 10% o valor {moeda.moeda(valor)} -> {moeda.aumentar(valor, False)} ')
print(f'Diminuindo 10% o valor {moeda.moeda(valor)} -> {moeda.diminuir(valor, False)} ')
print(f'O dobro do valor {moeda.moeda(valor)} -> {moeda.dobrar(valor, True)} ')
print(f'A metade do valor {moeda.moeda(valor)} -> {moeda.metade(valor, True)} ')
