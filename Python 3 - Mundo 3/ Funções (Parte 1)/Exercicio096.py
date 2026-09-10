def area(larg, compr):
    a = larg * compr
    print(f'A area de um terreno {larg} x {compr} é = {a}')


print('         Controle de Terrenos')
print('-' * 40)

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

area(largura, comprimento)

