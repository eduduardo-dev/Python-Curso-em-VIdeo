from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        print('Passo inválido! Usando passo 1.')
        passo = 1

        passo = abs(passo)

    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ')
            sleep(0.2)

    else:
        for c in range (inicio, fim - 1, -passo):
            print(c, end=' ')
            sleep(0.2)


print('A) Contagem de 1 até 10, de 1 em 1')
contador(1, 10, 1)

print('\nB) Contagem de 10 até 0, de 2 em 2')
contador(10, 0, 2)

print('\nC) Contagem personalizada')

inic = int(input('Inicio: '))
f = int(input('Fim: '))
pas = int(input('Passo: '))

contador(inic, f, pas)