from random import randint
Vitoria = 0
while True:
    print('Par ou Impar')

    Jogador = int(input('Digite um valor: '))
    Computador = randint(0, 10)

    Tot = Jogador + Computador

    Tipo = ' '
    while Tipo not in 'PI':
        Tipo = str(input('Par ou Impar?: ')).upper().strip()[0]
    print(f'Voce jogou {Jogador} e o computador jogou {Computador} \n'
            f'Total de {Tot}')
    if Tipo == 'P':
        if Tot % 2 == 0:
            print('Voce ganhou!!')
            Vitoria += 1
        else:
            print('Voce perdeu!!')
            break
    if Tipo == 'I':
        if Tot % 2 == 1:
            print('Voce ganhou!!')
            Vitoria += 1
        else:
            print('Voce perdeu!!')
            break

    print('Vamos jogar novamente')
print(f'Voce alcancou uma sequencia de {Vitoria} vezes')