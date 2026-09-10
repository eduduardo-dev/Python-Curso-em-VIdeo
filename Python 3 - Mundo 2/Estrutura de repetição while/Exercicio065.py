Num = int(input('Digite o 1º Valor: '))
Continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
Cont = 0
Seq = 1
MaiorNum = MenorNum = Num
Total = Num

while Continuar != 'N':
    Cont += 1
    Seq += 1
    Total += Num
    Media = Total / Cont
    Num = int(input('Digite o {}º Valor: '.format(Seq)))
    Continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if Num > MaiorNum:
        MaiorNum = Num
    elif Num < MenorNum:
        MenorNum = Num
print('O maior numero foi {} e o menor numero foi {}'.format(MaiorNum, MenorNum))
print('A media entre eles é {}'.format(Media))