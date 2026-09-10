from random import randint
from time import sleep
from operator import itemgetter

jogos = {'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6)}
ranking = dict()

print('Os valores sorteados foram: ')

for k, v in jogos.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

for j, n in enumerate(ranking):
    print(f'O {j+1}º lugar: {n[0]} com {n[1]}.')
    sleep(1)
