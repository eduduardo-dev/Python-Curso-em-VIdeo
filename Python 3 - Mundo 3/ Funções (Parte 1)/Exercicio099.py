from time import sleep

def maior(* num):
    maior = cont = 0
    print('\nAnalisando os valores passados...')

    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)

        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor

        cont += 1

    print(f'\nForam informados {cont} valores')
    print(f'O maior valor informado foi {maior}')

maior(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
maior(0, 2, 4, 6, 8, 10)
maior(2, 1, 8, 5, 0)
maior(9, 5, 8)
maior()