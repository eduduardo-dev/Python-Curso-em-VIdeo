from Exercicio115.Lib.Interface import *


def file_exists(name):
    try:
        file = open(name, 'rt')
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True

# 'wt+' siginica w = escrever um arquivo, t = em texto e + = e se ppr acaso o arquico nao existir ele cria
def create_file(name):
    try:
        file = open(name, 'wt+')
        file.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {name} criado com sucesso!')


def read_file(name):
    try:
        file = open(name, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in file:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        file.close()

# a aqui é de append = adicionar
def register_user(file_name, name='Desconhecido', age=0):
    try:
        file = open(file_name, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            file.write(f'{name};{age}\n')
        except:
            print('Houve um ERRO na na hora de escrever os dados!')
        else:
            print(f'Novo registro de {name} adicionado com sucesso!')
            file.close()