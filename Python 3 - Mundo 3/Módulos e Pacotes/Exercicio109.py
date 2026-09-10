from UtilidadesCeV import moeda

preco = float(input('Informe o preço: R$ '))

print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')

taxa = float(input('Informe a taxa '))

print(f'O preço de {moeda.moeda(preco)} apos diminuir {taxa}% fica {moeda.diminuir(preco, taxa, True)}')
print(f'O preço de {moeda.moeda(preco)} apos aumentar {taxa}% fica {moeda.aumentar(preco, taxa, True)}')

