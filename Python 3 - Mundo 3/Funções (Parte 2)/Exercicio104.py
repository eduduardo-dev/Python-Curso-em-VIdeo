def leiaInt(msg):
    while True:
        numero = input(msg)

        try:
            numero = int(numero)
            return numero
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")


number = leiaInt('Digite um numero inteiro: ')

print(f'Você digitou o numero {number}')