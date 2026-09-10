viagem = float(input('Qual é a distancia da viagem (em Km): '))

if viagem <= 200:
    tarifa1 = viagem * 0.50
    print('Tarifa de R$ 0,50 centavos por Km para viagens de ate 200Km de distancia!!! \n'
          'Por ser uma viagem de {} Km, voce ira pagar R$ {:.2f} reais na tarifa do onibus'.format(viagem, tarifa1))
else:
    tarifa2 = viagem * 0.45
    print('Tarifa de R$ 0,45 centavos por Km para viagens acima de 200Km de distancia!!! \n'
          'Por ser uma viagem de {} Km, voce ira pagar R$ {:.2f} reais na tarifa do onibus'.format(viagem, tarifa2))