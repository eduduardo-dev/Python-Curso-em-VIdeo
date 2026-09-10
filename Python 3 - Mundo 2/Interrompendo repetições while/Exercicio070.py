totalproduto = 0
produto1000 = 0

menorpreco = 0
nomepdtbarato = ''

cont = 1

while True:
    nomeproduto = str(input('Nome do produto: '))
    precoproduto = float(input('Qual o preço do produto: '))

    totalproduto += precoproduto

    if precoproduto >= 1000:
        produto1000 += 1

    if cont == 1:
        menorpreco = precoproduto
        nomepdtbarato = nomeproduto

    elif precoproduto < menorpreco:
        menorpreco = precoproduto
        nomepdtbarato = nomeproduto

    cont += 1

    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    while not continuar in 'SN':
        print('Resposta invalida. Tente novamente')
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if continuar == 'N':
        break

print('-' * 40)
print(f'Total da compra: R$ {totalproduto:.2f}')
print(f'{produto1000} produtos custam mais de R$1000')
print(f'O produto mais barato foi {nomepdtbarato}, custando R$ {menorpreco:.2f}')