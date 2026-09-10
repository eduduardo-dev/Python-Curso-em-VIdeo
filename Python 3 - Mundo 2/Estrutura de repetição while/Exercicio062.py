a1 = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razao: '))

# decimo = a1 + (10 - 1) * razao
cont = 1
termo = a1
decimo = 10

while cont <= decimo:
    print(' {} '.format(termo), end='→')
    termo += razao
    cont += 1

mais = int(input('\nQuantos termos deseja adicionar? '))
decimo += mais

while mais != 0:
    while cont <= decimo:
        print(' {} '.format(termo), end='→')
        termo += razao
        cont += 1

    mais = int(input('\nQuantos termos deseja adicionar? '))
    decimo += mais
    
print('FIM')