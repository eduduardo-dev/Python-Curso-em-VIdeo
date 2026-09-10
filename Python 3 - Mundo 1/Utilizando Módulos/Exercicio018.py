# import math
from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do angulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(' O valor do SENO é {:.2f} \n O valor do COSSENO é {:.2f} \n E o valor da TANGENTE é {:.2f}'.format(seno, cosseno, tangente))