valor1 = int(input('Digite o 1º valor: '))
valor2 = int(input('Digite o 2º valor: '))
valor3 = int(input('Digite o 3º valor: '))

maiorvalor = valor1
menorvalor = valor1

if valor2 > valor1 and valor2 > valor3:
    maiorvalor = valor2

if valor3 > valor1 and valor3 > valor2:
    maiorvalor = valor3

if valor2 < valor1 and valor2 < valor3:
    menorvalor = valor2

if valor3 < valor1 and valor3 < valor2:
    menorvalor = valor3

print('O maior valor é {} \n'
      'E o menor valor é {}'.format(maiorvalor, menorvalor))