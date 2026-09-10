matriz = [[], [], []]
SomaTerCol = 0
SomaPAR = 0
MaiorNumSegLin = 0

for l in range(0, 3):
    for c in range(0, 3):
        numeros = int(input(f'Digite um numero para a posição [{l}, {c}]: '))
        matriz[l].append(numeros)

        if numeros % 2 == 0:
            SomaPAR += numeros

        if c == 2:
            SomaTerCol += numeros

        if l == 1:
            if MaiorNumSegLin is None or numeros > MaiorNumSegLin: #verifica caso o usuario digitar numeros negativos
                MaiorNumSegLin = numeros

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma dos valores pares é {SomaPAR}.')
print(f'A soma dos valores da terceira coluna é {SomaTerCol}.')
print(f'O maior valor da segunda linha é {MaiorNumSegLin}.')