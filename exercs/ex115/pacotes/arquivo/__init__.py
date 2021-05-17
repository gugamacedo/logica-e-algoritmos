from pacotes.interface import mensagem

def file_ok(file):
    try:
        a = open(file, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_file(file):
    try:
        a = open(file, 'wt+')
        a.close()
    except:
        print('Erro ao criar o arquivo')
    else:
        print('Arquivo criado')

def ler_file(file):
    try:
        a = open(file, 'rt', encoding='utf-8')
    except:
        print('Erro ao ler o arquivo')
    else:
        mensagem('Pessoas cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(file, nome, idade):
    try:
        a = open(file, 'at', encoding='utf-8')
    except:
        print('Erro ao abrir arquivo')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Erro ao escrever no arquivo')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()