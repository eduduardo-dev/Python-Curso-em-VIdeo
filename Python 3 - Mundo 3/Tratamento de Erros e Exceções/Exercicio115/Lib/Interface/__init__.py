def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except KeyboardInterrupt:
            print("\033[0;31mO usuario preferiu nao informar um numero\033[m")
            return 0
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
            continue
        else:
            return numero


def linha(tam=40):
    return "~" * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[35mEscolha sua opção: \033[m')
    return opc