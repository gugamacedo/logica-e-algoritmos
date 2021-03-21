'''
print('Estou aprendendo Python!')
# Print é uma Função. Aspas transforma em texto. #Transforma em comentário
# Para escrever algo na tela, sempre: print(‘Mensagem’)

print(7 + 4)
# Para calculadores sem aspas

print('7' + '4')
# Assim ele soma as mensagens como textos

print('Cinco ' + '5')
>> Cinco5
print('Cinco ', '5')
Cinco 5

# Durante variáveis, funções, etc, sempre usar letra snake_case
# No caso do Python toda variável é um objeto. 
# Leia o = como recebe no caso das variáveis

nome = 'Jubisvaldo'
idade = 30
apelido = 'jubi'
print(f'Olá {nome}! Ou posso te chamar de {apelido}...? {idade} anos, trintou!)

# Função input significa leia. Para criar interatividade com o usuário vamos atribuir input nas variáveis:
nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')
print(nome, idade)
'''