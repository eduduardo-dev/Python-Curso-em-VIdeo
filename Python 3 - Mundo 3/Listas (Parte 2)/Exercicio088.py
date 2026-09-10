from random import randint
from time import sleep

jogos = list()

QuantJogos = int(input("Quantos jogos deseja sortear? "))

print(f'\nSorteando {QuantJogos} Jogos...')
sleep(1)

for i in range(0, QuantJogos):
    numeros = list()

    while len(numeros) < 6:
        numero = randint(1, 60)

        if numero not in numeros:
            numeros.append(numero)

    numeros.sort()
    jogos.append(numeros)

    print(f'Jogo {i + 1}: {numeros}')
    sleep(1)

print('\nBoa sorte!')