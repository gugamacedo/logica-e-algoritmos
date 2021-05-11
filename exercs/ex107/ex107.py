# Crie um módulo chamado moeda.py que tenhas as funções incorporadas aumentar() diminuir() dobro() metade()
# Faça um programa que importe esse módulo e use essas funções
import moeda

valor = float(input('Digite um valor: R$'))

print()
print(f'Aumentando 10% o valor R${valor} -> R${moeda.aumentar(valor)} ')
print(f'Diminuindo 10% o valor R${valor} -> R${moeda.diminuir(valor)} ')
print(f'O dobro do valor R${valor} -> R${moeda.dobrar(valor)} ')
print(f'A metade do valor R${valor} -> R${moeda.metade(valor)} ')
