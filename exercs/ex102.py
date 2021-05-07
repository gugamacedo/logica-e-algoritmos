# Faça uma função fatorial() que receba 2 parâmetros: :número: a calcular e :show: (opcional), que será um valor lógico, indicando se será mostrado ou não na tela o processo de cálculo do fatorial; e tem que documentar
def fatorial(num, show):
    """
    -> A função calcula o fatorial e, se o user quiser, retorna todo processo
    :num: recebe o número para calcular fatorial
    :show: diz se o user quer ou não er o processo
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == 'S':
            print(c, end='')
            print(' x ' if c > 1 else ' = ', end='')
    return f


num = int(input('Digite um número: '))
show = str(input('Quer ver todo processo [S/N]? ')).upper()
while 'S' != show != 'N':
    show = str(input('Quer ver todo processo [S/N]? ')).upper()

print(fatorial(num, show))
