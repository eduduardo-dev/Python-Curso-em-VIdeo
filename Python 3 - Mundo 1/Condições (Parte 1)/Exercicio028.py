import random

numero = random.randint(1, 5)

escolha_user = int(input('Escolha um numero de 1 a 5: '))

if escolha_user == numero:
    print('Parabens!! era exatamente no numero {} que eu estava pensando'.format(numero))
else:
    print('HAHAHA!! Não foi esse numero no qual eu estava pensando ({})'.format(numero))