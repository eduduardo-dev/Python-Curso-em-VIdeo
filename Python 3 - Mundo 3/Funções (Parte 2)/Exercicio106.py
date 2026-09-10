from time import sleep
cores = (
    '\033[m',          # 0 - padrão
    '\033[1;30;41m',   # 1 - preto/vermelho
    '\033[1;30;42m',   # 2 - preto/verde
    '\033[1;30;43m',   # 3 - preto/amarelo
    '\033[1;30;44m',   # 4 - preto/azul
    '\033[1;30;45m',   # 5 - preto/magenta
    '\033[1;30;46m',   # 6 - preto/ciano
    '\033[1;30;47m',   # 7 - preto/branco
)


def ajuda(command):
    titulo(f'Acessando o manual do \'{command}\'', 4)
    print(cores[5], end='')
    help(command)
    print(cores[5], end='')
    sleep(0.8)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'{msg.center(tam)}')
    print('~' * tam)
    print(cores[0], end='')
    sleep(0.5)

# programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYhelp', 2)
    comando = str(input('Função ou Biblioteca >> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Ate Logo!', 1)