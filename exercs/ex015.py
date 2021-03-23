# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quatindade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, savbendo que o carro custa R$60 por dia e R$0,15 por Km rodado
kilometragem = float(input('Quantos kilômetros você rodou? '))
diaria = int(input('E por quantos dias alugou? '))
print(f'Você tem que pagar R${round(kilometragem * 0.15 + diaria * 60, 2)}')
