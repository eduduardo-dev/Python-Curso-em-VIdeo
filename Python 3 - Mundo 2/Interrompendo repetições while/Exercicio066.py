Num = int(input('Digite um numero: '))
Total = Cont = 0
while True:
    Cont += 1
    Total += Num
    Num = int(input('Digite um numero: '))
    if Num == 999:
        break
print('Voce digitou {} e a soma entre eles é {}'.format(Cont, Total))