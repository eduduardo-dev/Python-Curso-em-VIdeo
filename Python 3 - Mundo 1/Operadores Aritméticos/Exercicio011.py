largura = float(input('Qual a largura da parede: '))
altura = float(input('Qual a altura da parede: '))

area = largura * altura
tinta = area / 2

print(' A area dessa parede a ser pintada é {:.2f} \n e sera necessario {:.2f}l de tinta para pinta-la por inteiro'.format(area, tinta))