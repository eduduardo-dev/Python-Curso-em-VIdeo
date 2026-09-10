# a1 = int(input('Informe o primeiro termo: '))
# razao = int(input('Informe a razao: '))
# decimo = a1 + (10 - 1) * razao
# for c in range(a1, decimo + 1, razao):
#     print(' {} '.format(c), end='→')

a1 = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razao: '))
decimo = a1 + (10 - 1) * razao
c = a1
while c <= decimo:
    print(' {} '.format(c), end='→')
    c += razao