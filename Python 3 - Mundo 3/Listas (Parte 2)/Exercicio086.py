matriz = [[], [], []]

for l in range(0, 3):
    for c in range(0, 3):
        numeros = int(input(f'Digite um numero para a posição [{l}, {c}]: '))
        matriz[l].append(numeros) 

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()