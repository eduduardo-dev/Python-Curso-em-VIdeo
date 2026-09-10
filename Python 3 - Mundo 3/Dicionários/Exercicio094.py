pessoa = dict()
galera = list()

soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).capitalize()

    while True:
        pessoa['genero'] = str(input('Genero [M/F]: ')).strip().upper()[0]
        if pessoa['genero'] not in 'MF':
            print('Resposta inválida. Digite apenas M ou F.')
        else:
            break

    pessoa['idade'] = int(input('Idade: '))

    soma += pessoa['idade']

    galera.append(pessoa.copy())

    while True:
        pergunta = input('Quer continuar? [S/N] ').strip().upper()[0]

        if pergunta not in 'SN':
            print('Resposta inválida. Digite apenas Sim ou Não.')
        else:
            break

    if pergunta == 'N':
        break

print('-' * 30)
print(f'A) Foram cadastradas {len(galera)} pessoas.')

media = soma / len(galera)

print(f'B) A media de idade é {media:.2f} anos.')

print('C) As mulheres cadastradas foram: ')
for p in galera:
    if p['genero'] == 'F':
        print(f' {p["nome"]}')

print('D) Lista das pessoas acima da media de idade:')
for p in galera:
    if p['idade'] > media:
        print(f' {p["nome"]} - {p["idade"]} anos')