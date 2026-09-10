dados = list()
geral = list()


while True:
    dados.append(str(input('Digite seu nome: ')).capitalize())
    dados.append(float(input(f'Digite sua 1º nota: ')))
    dados.append(float(input(f'Digite sua 2º nota: ')))
    geral.append(dados[:])
    dados.clear()

    while True:
        pergunta = input('Quer continuar? [S/N] ').strip().upper()[0]

        if pergunta not in 'SN':
            print('Resposta inválida. Digite apenas Sim ou Não.')
        else:
            break

    if pergunta == 'N':
        break

print('\n' + '=' * 40)
print('                 BOLETIM')
print('=' * 40)

print(f'{"Nº":<5} {"NOME":<20} {"MÉDIA":>10}')
print('-' * 40)

for posicao, aluno in enumerate(geral):
    media = (aluno[1] + aluno[2]) / 2
    print(f'{posicao:<5} {aluno[0]:<20} {media:>10.1f}')

print('=' * 40)


while True:
    opcao = int(input('\nDigite o número do aluno para consultar [999 para sair]: '))

    if opcao == 999:
        print('Programa encerrado. Até mais!')
        break

    if opcao < 0 or opcao >= len(geral):
        print('Aluno inválido! Tente novamente.')

    else:
        aluno = geral[opcao]

        print('\n' + '-' * 30)
        print(f'Aluno: {aluno[0]}')
        print(f'1ª Nota: {aluno[1]}')
        print(f'2ª Nota: {aluno[2]}')
        print('-' * 30)