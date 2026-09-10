radar = float(input('Qual a velocidade do carro? '))

multa = (radar - 80) * 7

if radar > 80:
    print('Você foi multado!! '
          'Por estar acima do limite de velocidade (80km/h) voce foi multado em R$ {:.2f} reais. \n'
          'º Multa de R$ 7,00 reais a cada 1km/h acima do limite da via \n'
          'E voce estava a {:.2f}'.format(multa, radar))
else:
    print('Voce esta dentro do limite de velocidade \n'
          'Prossiga tranquilamente, respeitando as regras de transito')