print('Tabuada')
Num = 1
Tabuada = 1

while True:
    Num = int(input('Digite um numero: '))

    if Num < 0:
        break

    Cont = 1

    while Cont <= 10:
        Tabuada = Num * Cont
        print(f'{Num} x {Cont} = {Tabuada}')
        Cont += 1