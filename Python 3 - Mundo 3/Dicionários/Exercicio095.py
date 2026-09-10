jogador = dict()
Aproveitamento_geral = list()
partidas = list()

while True:
    jogador.clear()
    partidas.clear()

    jogador['Nome'] = str(input('Nome do jogador: ')).capitalize()
    totpartidas = int(input(f'Quantas partida {jogador["Nome"]} jogou? '))

    for c in range(1, totpartidas + 1):
        partidas.append(int(input(f'Quantos gols na {c}º partida ? ')))

    jogador['Gols'] = partidas[:]
    jogador['TotGols'] = sum(partidas)

    Aproveitamento_geral.append(jogador.copy())

    while True:
        pergunta = input('Quer continuar? [S/N] ').strip().upper()[0]

        if pergunta not in 'SN':
            print('Resposta inválida. Digite apenas Sim ou Não.')
        else:
            break

    if pergunta == 'N':
        break

artilharia = sorted(Aproveitamento_geral,
    key=lambda jogadores: jogadores['TotGols'],
    reverse=True
)

print('-' * 40)
print('                 ARTILHARIA')
print('-' * 40)

print(f'{"Nº":<5} {"NOME":<20} {"GOLS":>10}')
print('-' * 40)

for posicao, jogador in enumerate(artilharia):
    print(f'{posicao + 1:<5} {jogador["Nome"]:<20} {jogador["TotGols"]:>10}')

print('-' * 40)

while True:

    opcao = int(input('\nDigite o número do jogador para consultar [999 para sair]: '))

    if opcao == 999:
        print('Programa encerrado. Até mais!')
        break

    if opcao < 0 or opcao >= len(artilharia):
        print('Jogador inválido! Tente novamente.')

    else:
        jogador = artilharia[opcao]

        print('\n' + '-' * 30)
        print(f'Jogador: {jogador["Nome"]}')
        print(f'Total de gols: {jogador["TotGols"]}')
        print('-' * 30)

        for i, c in enumerate(jogador['Gols']):
            print(f'  -> Na partida {i + 1}, fez {c} gols.')

        print('-' * 30)