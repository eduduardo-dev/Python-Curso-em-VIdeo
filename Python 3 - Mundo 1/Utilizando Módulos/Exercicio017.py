# // Forma 1 de resolver
#
# co = float(input('Informe o valor do cateto oposto: '))
# ca = float(input('Informe o valor do cateto oposto: '))
#
# hi = (ca**2 + co**2) ** (1/2)
#
# print('O valor da hipotenusa é {:.2f}'.format(hi))

# // Forma 2 de resolver
# import math
#
# cat_oposto = float(input('Informe o valor do cateto oposto: '))
# cat_adj = float(input('Informe o valor do cateto adjacente: '))
#
# hip = (math.pow(cat_oposto,2) + math.pow(cat_adj,2))
# hip = math.sqrt(hip)
#
# print('O valor da hipotenusa é {}'.format(hip))

# // Forma 3 de resolver

# import math
from math import hypot

ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))

# hi = math.hypot(ca, co)
hi = hypot(ca, co)

print('O valor da hipotenusa é {:.2f}'.format(hi))