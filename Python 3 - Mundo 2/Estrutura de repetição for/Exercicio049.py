valor = int(input('Digite um valor: '))
print('Tabuada!!!')
for c in range(1, 10 + 1):
    tab = valor * c
    print('{} x {} = {}'.format(valor, c, tab))