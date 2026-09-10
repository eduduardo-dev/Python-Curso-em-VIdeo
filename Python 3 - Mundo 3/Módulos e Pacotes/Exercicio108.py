from UtilidadesCeV import moeda

preco = float(input('Informe o preço: R$ '))

print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')

taxa = float(input('Informe a taxa '))

print(f'O preço de {moeda.moeda(preco)} apos diminuir {taxa}% fica {moeda.moeda(moeda.diminuir(preco, taxa))}')
print(f'O preço de {moeda.moeda(preco)} apos aumentar {taxa}% fica {moeda.moeda(moeda.aumentar(preco, taxa))}')

