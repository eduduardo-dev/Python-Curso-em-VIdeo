lista_geral = []
lista_pares = []
lista_impar = []

while True:
    valor = int(input('Digite um valor: '))

    lista_geral.append(valor)

    if valor % 2 == 0:
        lista_pares.append(valor)

    else:
        lista_impar.append(valor)

    while True:
        pergunta = input('Quer continuar? [S/N] ').strip().upper()[0]

        if pergunta not in 'SN':
            print('Resposta inválida. Digite apenas Sim ou Não.')
        else:
            break

    if pergunta == 'N':
        break

print(f'A lista completa é {lista_geral}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de impares é {lista_impar}')