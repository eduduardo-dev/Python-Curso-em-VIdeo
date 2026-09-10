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

def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg))
        except KeyboardInterrupt:
            print("\033[0;31mO usuario preferiu nao informar um numero\033[m")
            return 0
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite um número real válido.\033[m")
            continue
        else:
            return numero


numberInt = leiaInt('Digite um numero inteiro: ')
numberFloat = leiaFloat('Digite um numero real: ')
print(f'O valor inteiro digitado foi {numberInt} e o real foi {numberFloat}')