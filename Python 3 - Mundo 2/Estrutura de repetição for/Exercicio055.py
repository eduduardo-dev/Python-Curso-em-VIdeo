# peso = float(input('(1º pessoa) Digite o seu peso: '))
#
# menor_peso = peso
# maior_peso = peso
#
# for cont in range(2, 5 + 1):
#     peso = float(input('({}º pessoa) Digite o seu peso: '.format(cont)))
#
#     if peso > maior_peso:
#         maior_peso = peso
#     elif peso < menor_peso:
#         menor_peso = peso
#
# print(maior_peso)
# print(menor_peso)

maiorpeso = 0
menorpeso = 0

for cont in range(1, 5 + 1):
    peso = float(input('({}º pessoa) Digite o seu peso: '.format(cont)))
    if cont == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print('O maior peso lido foi {} Kg'.format(maiorpeso))
print('O menor peso lido foi {} Kg'.format(menorpeso))