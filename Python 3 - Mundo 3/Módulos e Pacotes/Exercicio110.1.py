from UtilidadesCeV import moeda


preco = float(input('Informe o preço: R$ '))
aumento = float(input('Taxa de aumento: '))
diminuicao = float(input('Taxa de diminuição: '))

moeda.resumo(preco, aumento, diminuicao)