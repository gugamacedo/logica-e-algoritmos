# Crie a função vota() que vai receber ano de nascimento, e retornar se o voto é obrigatório, negado ou opcional, junto com a idade da pessoa, numa frase
def vota(idade):
    from datetime import date  # você pode chamar o import dentro da função, se só irá usar aqui entro, no block scope, isso também ajuda a economizar memória, já que só funcionará dentro desse escopo
    idade = date.today().year - idade
    if idade <= 15:
        return f'Aos {idade} anos o voto é negado!'
    elif 17 == idade == 16 or idade >= 65:
        return f'Aos {idade} anos o voto é opcional!'
    elif idade >= 18:
        return f'Aos {idade} anos o voto é obrigatório'


print(vota(idade = int(input('Digite seu ano de nascimento: '))))