from UtilidadesCeV import moeda

preco = float(input('Informe o preço: R$ '))

print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'O dobro de {preco} é {moeda.dobro(preco)}')

taxa = float(input('Informe a taxa '))

print(f'O preço de {preco} apos diminuir {taxa}% fica {moeda.diminuir(preco, taxa)}')
print(f'O preço de {preco} apos aumentar {taxa}% fica {moeda.aumentar(preco, taxa)}')

