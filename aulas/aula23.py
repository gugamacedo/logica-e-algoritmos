# Exceções: erros semânticos (nameError, TypeError, IndexError, )
# Tipo quando você digita string em int, o contrário, input vazio, divisão por zero, etc

# Tratamento de erros
try:  # tente isso
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
# except:  # se der erro
# except Exception as erro:
#     print(f'Problema encontrado: {erro}')
# pode ter vários except
# except Exception as erro:
#     print(f'Problema encontrado: {erro.__cause__}')
except (ValueError, TypeError):
    print('Problema com os tipos de dados inseridos')
except ZeroDivisionError:
    print('Não se divide por zero')
except KeyboardInterrupt:
    print('Usuário não inseriu os dados')
else:  # retornar isso se não der erro. Opcional 
    print(r)
finally:  # acontecerá independente de qlq coisa. Opcional também
    print('Volte Sempre')