# Crie uma lista, onde o user vai inserir 7 números.
# Nessa lista teram duas lisats internas, uma com os números pares, outra com os ímpares.
# No fim exiba as duas listas, com os números em ordem crescente
nums = [[], []]
for c in range(1, 8):
    user_nums = int(input(f'Digite o {c}º número: '))
    if user_nums % 2 == 0:
        nums[0].append(user_nums)
    else:
        nums[1].append(user_nums)
print('-=-'*10)
print(f'Números pares: {sorted(nums[0])}\nNúmeros ímpares: {sorted(nums[1])}') 
# Lembrando que o .sort() altera a lista, jáo sorted só exibe ela em ordem momentaneamente
