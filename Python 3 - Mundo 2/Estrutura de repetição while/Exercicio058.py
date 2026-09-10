import random

numero1a10 = random.randint(0, 10)
tottentativas = 0
escolha_user = int(input('Escolha um numero de 1 a 10: '))

while escolha_user != numero1a10:
    print('HAHAHA, numero errado. Tente novamente!!')
    escolha_user = int(input('Escolha um numero de 1 a 10: '))
    tottentativas += 1

print('Finalmenteeee!!! Ja estava ficando cansado hahahahah \n'
      'Esse foi o seu numero de tentativas {}'.format(tottentativas))