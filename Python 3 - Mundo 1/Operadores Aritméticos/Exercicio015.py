km = float(input('Foi percorrido quantos KMs pelo carro? '))
dias = int(input('Por quantos dias ele foi ou vai ser alugado? '))

preco_dias = dias * 60
preco_km = km * 0.15
total = preco_dias + preco_km

print(' Considerando que foi percorrido {} Kms por {} dias, o valor a ser pago é R$ {:.2f} \n (Valor calculado de Km rodados é {} e por dias usados é {})'.format(km, dias, total, preco_km, preco_dias))