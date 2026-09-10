preco = float(input('Qual o preço do produto: '))

novopreco = preco - (preco * 5 / 100)

print('o novo valor do produto ja com 5% de desconto fica {:.2f}'.format(novopreco))