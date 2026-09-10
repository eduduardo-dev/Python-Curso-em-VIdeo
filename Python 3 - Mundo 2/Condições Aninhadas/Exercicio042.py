A = float(input('Digite o comprimento do segmento "A": '))
B = float(input('Digite o comprimento do segmento "B": '))
C = float(input('Digite o comprimento do segmento "C": '))

if A + B > C and A + C > B and B + C > A:
    print('Os tres segmentos acima podem formar um triangulo!!! \n'
          'Ja que {}, {} e {} respeitam a regra da desigualdade triangular'. format(A, B, C))
    if A == B == C:
        print('E formam um TRIÂNGULO EQUILÁTERO!!!')
    elif A != B != C != A:
        print('E formam um TRIÂNGULO ESCALENO!!!')
    else:
        print('E formam um TRIÂNGULO ISÓSCELES!!!')
else:
    print('Os tres segmentos acima não podem formar um triangulo!!! \n'
          'Ja que {}, {} e {} não respeitam a regra da desigualdade triangular'. format(A, B, C))