from random import randint

numeros = list()

def sorteia():
    for cont in range(5):
        numeros.append(randint(1, 10))

def somaPar():
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero

    print(f'Somando os valores pares de {numeros}, temos {soma}')

sorteia()
print(f'Sorteando os 5 valores da lista: {numeros} PRONTO!')
somaPar()