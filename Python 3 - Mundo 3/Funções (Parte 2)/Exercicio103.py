def ficha(name='<desconhecido>', goals=0):
    print(f'O jogador {name} fez {goals} gol(s) no campeonato.')

nome = str(input('Nome do jogador: '))
if nome == '':
    nome = '<desconhecido>'

# serve para impedir que o programa quebre caso o usuário informe um valor inválido.
try:
    gols = int(input('Quantidade de gols: '))
except ValueError:
    gols = 0

ficha(nome, gols)