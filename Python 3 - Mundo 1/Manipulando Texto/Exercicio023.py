valor = int(input('Digite um valor: '))
u = valor // 1 % 10
d = valor // 10 % 10
c = valor // 100 % 10
m = valor // 1000 % 10

print('Analisando o numero {}: '.format(valor))
print('Unidade: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhar: {}'.format(m))