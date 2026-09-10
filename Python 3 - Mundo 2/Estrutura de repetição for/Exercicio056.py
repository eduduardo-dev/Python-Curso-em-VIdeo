soma_idade = 0
media_idade = 0
mais_velho = 0
nome_velho = ''
mulheres20 = 0

for cont in range(1, 5):
    print('----- {}º Pessoa -----'.format(cont))
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper()

    soma_idade += idade

    if cont == 1 and sexo == 'M':
        mais_velho = idade
        nome_velho = nome

    if sexo == 'M' and idade > mais_velho:
        mais_velho = idade
        nome_velho = nome

    if sexo == 'F' and idade < 20:
        mulheres20 += 1

media_idade = soma_idade / 4
print('A media de idade do grupo é {} anos'.format(media_idade))
print('O homem mais velho é {} com {} anos'.format(nome_velho, mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres20))