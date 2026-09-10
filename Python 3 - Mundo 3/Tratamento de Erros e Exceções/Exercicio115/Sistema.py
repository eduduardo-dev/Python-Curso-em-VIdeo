from Exercicio115.Lib.Interface import *
from Exercicio115.Lib.Arquivo import *
from time import sleep

arquivo = 'cursoemvideo.txt'

if not file_exists(arquivo):
    create_file(arquivo)
    sleep(1)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Novas Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # opção de listar o conteudo de um arquivo
        read_file(arquivo)
    elif resposta == 2:
        #opção de cadastrar nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        register_user(arquivo, nome, idade)
    elif resposta == 3:
        print('Saindo do Sistema... Ate Logo!!')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida!\033[m')
        sleep(1)