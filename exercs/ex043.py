'''Calcule o imc e mostre seu status IMC: peso/altura*altura
até 18.5 abaixo do peso, até 25 peso ideal, até 30 sobrepeso, até 40 obesidade, acima de 40 obesidade mórbida'''
weight = float(input('Digite seu peso: '))
height = float(input('Digite sua altura: '))
imc = weight/height**2
print(f'Seu IMC é de {imc:.1f}\n')
if imc <= 18.5:
    print('Você está abaixo do peso ideal.')
elif imc <= 25:
    print('Peso ideal, parabéns!')
elif imc <= 30:
    print('Está um pouco acima do peso ideal.')
elif imc <= 40:
    print('Você está obeso, muito acima do peso ideal!')
else:
    print('Você está com obesidade mórbida, corra pro médico!')
