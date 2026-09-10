Valor = int(input('Informe o valor: '))
Cont = Valor
Fat = 1
print('{}! = Calculando...'.format(Valor))
while Cont > 0:
    print('{} '.format(Cont), end='')
    print('x ' if Cont > 1 else '= ', end='')

    Fat *= Cont
    Cont -= 1

print('{}'.format(Fat))