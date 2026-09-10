dados = list()
geral = list()

while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    geral.append(dados[:])
    dados.clear()

    while True:
        pergunta = input('Quer continuar? [S/N] ').strip().upper()[0]

        if pergunta not in 'SN':
            print('Resposta inválida. Digite apenas Sim ou Não.')
        else:
            break

    if pergunta == 'N':
        break

print(f'{len(geral)} pessoas cadastradas.')

maiorp = geral[0][1]
menorp = geral[0][1]

for pessoa in geral:
    if pessoa[1] > maiorp:
        maiorp = pessoa[1]

    if pessoa[1] < menorp:
        menorp = pessoa[1]

print(f'O maior peso foi de {maiorp}Kg. As pessoas mais pesadas foram: ', end='')

for pessoa in geral:
    if pessoa[1] == maiorp:
        print(f'{pessoa[0]}... ', end='')

print()

print(f'O menor peso foi de {menorp}Kg. As pessoas menos pesadas foram: ', end='')

for pessoa in geral:
    if pessoa[1] == menorp:
        print(f'{pessoa[0]}... ', end='')