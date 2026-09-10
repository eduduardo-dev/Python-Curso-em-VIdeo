maioridade = 0
tothomens = 0
mulheres20 = 0
idade = 0
sexo = ''
cont = 1

while True:
    print(f'----- {cont}º Pessoa -----')
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]

    while sexo not in 'MF':
        print('Sexo inválido. Tente novamente.')
        sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]

    cont += 1

    if idade >= 18:
        maioridade = maioridade + 1

    if sexo == 'M':
        tothomens = tothomens + 1

    if sexo == 'F' and idade < 20:
        mulheres20 = mulheres20 + 1

    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    while not continuar in 'SN':
        print('Resposta invalida. Tente novamente')
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if continuar == 'N':
        break

print(f'maior de idade: {maioridade} \n'
      f'total de homens: {tothomens} \n'
      f'mulheres de 20: {mulheres20} \n')

# soma_idade = 0
# media_idade = 0
# mais_velho = 0
# nome_velho = ''
# mulheres20 = 0
#
# for cont in range(1, 5):
#     print('----- {}º Pessoa -----'.format(cont))
#     nome = str(input('Digite o seu nome: '))
#     idade = int(input('Digite a sua idade: '))
#     sexo = str(input('Digite o sexo [M/F]: ')).upper()
#
#     soma_idade += idade
#
#     if cont == 1 and sexo == 'M':
#         mais_velho = idade
#         nome_velho = nome
#
#     if sexo == 'M' and idade > mais_velho:
#         mais_velho = idade
#         nome_velho = nome
#
#     if sexo == 'F' and idade < 20:
#         mulheres20 += 1
#
# media_idade = soma_idade / 4
# print('A media de idade do grupo é {} anos'.format(media_idade))
# print('O homem mais velho é {} com {} anos'.format(nome_velho, mais_velho))
# print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres20))