# sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
#
# while sexo != 'M' and
#
# sexo != 'F':
#     print('Sexo invalido')
#     sexo = str(input('Informe seu sexo novamente: [M/F] ')).strip().upper()[0]

r = str(input('Digite seu sexo [M/F]: ')).strip().upper()
while r != 'M' and r != 'F':
    print('Você não digitou M ou F')
    r = str(input('Digite seu sexo [M/F]: ')).strip().upper()