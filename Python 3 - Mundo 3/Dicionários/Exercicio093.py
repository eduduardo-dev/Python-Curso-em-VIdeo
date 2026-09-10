Aproveitamento = dict()
partidas = list()

Aproveitamento['Nome'] = str(input('Nome do jogador: ')).capitalize()
totpartidas = int(input(f'Quantas partida {Aproveitamento["Nome"]} jogou? '))

for c in range(1, totpartidas + 1):
    partidas.append(int(input(f'Quantos gols na {c}º partida ? ')))

Aproveitamento['Gols'] = partidas[:]
Aproveitamento['TotGols'] = sum(partidas)

print('-'*20)
print(Aproveitamento)
print('-'*20)

for k, v in Aproveitamento.items():
    print(f'O campo {k} tem o valor {v}')
print('-'*20)

print(f'O jogador {Aproveitamento["Nome"]} jogou {len(Aproveitamento["Gols"])} partidas.')

for i, c in enumerate(Aproveitamento['Gols']):
    print(f'  -> Na partida {i+1}, fez {c} gols.')
print(f'Foi um total de {Aproveitamento["TotGols"]} gols.')