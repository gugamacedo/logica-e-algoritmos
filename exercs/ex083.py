# Leia uma expressão matemática e diga se tem parenteses faltando, se tiver a expressão é invalida, do contrário válida
count = pos = 0
expr = list(str(input('Digite uma expressão matemática: ')))
for i, v in enumerate(expr):
    if v == '(':
        count += 1
        pos += -i
    elif v == ')':
        count += -1
        pos += i
print('Expressão válida!' if pos > 1 and count == 0 else 'Expressão inválida!')
