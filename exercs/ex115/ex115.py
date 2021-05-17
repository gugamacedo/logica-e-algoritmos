# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simplmes.
# O sistema terá 3 opções: listar todas pessoas cadastradas, cadastrar e sair
from pacotes.interface import *
from pacotes.arquivo import *
from time import sleep

file = 'ex115/cadastros.txt'
if not file_ok(file):
    criar_file(file)

while True:
    resposta = options(['Listar pessoas', 'Cadastrar pessoa', 'Encerrar programa'])
    if resposta == 1:
        ler_file(file)
    elif resposta == 2:
        mensagem('Nova Cadastro')
        nome = str(input('Nome: ')).title()
        idade = leia_int('Idade: ')
        cadastrar(file, nome, idade)
    elif resposta == 3:
        mensagem('Encerrando sistema...')
        sleep(1)
        break
    else:
        mensagem('\033[31mEssa opção não existe\033[m')
        sleep(1)
