Valores = int(input('Digite um valor: '))
Total = Cont = 0
while Valores != 999:
    Total += Valores
    Cont += 1
    Valores = int(input('Digite um valor: '))
print('Voce digitou {} e a soma entre eles é {}'.format(Cont, Total))

