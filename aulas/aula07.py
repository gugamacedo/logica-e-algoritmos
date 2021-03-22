'''
Operadores aritméticos:

+ adição
- subtração
* multiplicação
/ divisão
** potênciação
// divisão inteira
% resto da divisão

Ordem de precedência:
()
**
* / // %    Quem vier primeiro
+ -         Quem vier primeiro


'''

num1 = int(input('Diz algum número\n'))
num2 = int(input('Diz outro número:\n'))
soma = num1+num2
subt = num1-num2
div = num1/num2
mult = num1*num2
potn = num1**num2
divint = num1//num2
divrest = num1%num2
print(f'A soma é {soma}\nA subtração é {subt}\nA divisâo é {div:.2f}\nA multiplicação é {mult}\n'
      f'A potenciação é {potn}\nA divisão inteira é {divint}\nO resto da divisão é {divrest}')
