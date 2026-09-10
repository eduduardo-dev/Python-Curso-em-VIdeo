def metade(number=0, formato=False):
    resultado = number / 2

    if formato:
        return moeda(resultado)
    else:
        return resultado


def dobro(number=0, formato=False):
    resultado = number * 2

    if formato:
        return moeda(resultado)
    else:
        return resultado


def aumentar(number=0, rate=0, formato=False):
    resultado = number + (number * rate / 100)

    if formato:
        return moeda(resultado)
    else:
        return resultado


def diminuir(number=0, rate=0, formato=False):
    resultado = number - (number * rate / 100)

    if formato:
        return moeda(resultado)
    else:
        return resultado


def moeda(number=0, coin='R$ '):
    return f'{coin}{number:.2f}'.replace('.', ',')


def resumo(num=0, increase=0, decrease=0, formato=False):
    print('~'*30)
    print('Resumo do valor'.center(30))
    print('~'*30)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Alta pós-{increase}%: \t{aumentar(num, increase, True)}')
    print(f'Caiu pós-{decrease}%: \t{diminuir(num, decrease, True)}')
    print('~'*30)

