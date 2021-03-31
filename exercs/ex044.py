''' Calcule o valor a ser pago por um produto, considerando o seu 'preço normal' e 'condição de pagamento'
A vista no dinheiro ou cheque: 10% de ddesconto. A vista no cartão 5%.
2x no cartao preço normal, 3x ou mais no cartão, 20% de juros '''
price = float(input('Digite o preço do produto: R$'))
choice = int(input(f'( 1 )     A vista no boleto: 10% de desconto -R${price*0.10:.2f} \n'
                   f'( 2 )     A vista no cartão: 15% de desconto -R${price*0.15:.2f}\n'
                   f'( 3 )     Em 2 vezes no cartão preço normal, sem desconto\n'
                   f'( 4 )     Em 3 vezes ou mais no cartão, com 20% de juros\n'
                   f'Digite a opção escolhida: '))
if choice == 1:
    print(f'\nSairá por R${price-price*0.10:.2f} á vista no boleto.')
elif choice == 2:
    print(f'\nSairá por R${price-price*0.15:.2f} á vista no cartão')
elif choice == 3:
    print(f'\nSairá por 2 vezes de R${price/2:.2f}')
elif choice == 4:
    choice = int(input('Em quantas vezes (com juros)? '))
    print(f'\nSairá por {choice} vezes de R${price * 1.20 / choice:.2f}. R${price * 1.20:.2f} no total')
else:
    print('\nOpção inválida!')
