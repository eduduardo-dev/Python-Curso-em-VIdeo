aluno = dict()

aluno['nome'] = str(input('Digite seu nome: ')).capitalize()

while True:
    try:
        # Tenta ler a média como número decimal
        aluno['Media'] = float(input(f'Média de {aluno['nome']}: '))

        # Se deu certo, agora valida se está no limite permitido
        if aluno['Media'] > 10 or aluno['Media'] < 0:
            print('Resposta inválida. Digite apenas uma Media entre 0 e 10.')

        else:
            break # Sai do laço se o número for válido

    except ValueError:
        # Executado caso o usuário digite letras ou símbolos
        print('Resposta inválida. Digite apenas Números.')

print(f'Nome é igual a {aluno['nome']}')
print(f'Média é igual a {aluno['Media']}')

if aluno['Media'] >= 7:
    print('Situação é igual a Aprovado!')
elif aluno['Media'] >= 5:
    print('Situação é igual a Recuperação')
else:
    print('Situação é igual a Reprovado!')