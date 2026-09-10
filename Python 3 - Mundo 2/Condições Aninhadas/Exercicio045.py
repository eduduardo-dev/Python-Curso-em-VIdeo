from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

#

print('''Escolha sua opção:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input('Sua jogada vai ser: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('O computador jogou {} \n'
      'O jogador jogou {}'.format(itens[computador], itens[jogador]))

if computador == jogador:
    print('EMPATE!!!')

elif ((jogador == 0 and computador == 2)
      or (jogador == 1 and computador == 0)
      or (jogador == 2 and computador == 1)):
    print('JOGADOR VENCEU!!!')

else:
    print('COMPUTADOR VENCEU!!!')