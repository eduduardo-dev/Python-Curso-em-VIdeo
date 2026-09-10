valores = []

while True:
    valor = int(input('Digite um valor: '))

    valores.append(valor)
    valores.sort(reverse=True)

    while True:
        pergunta = input('Quer continuar? [S/N] ').strip().upper()[0]

        if pergunta in ['S']:
            break

        elif pergunta in ['N']:
            break

        else:
            print('Resposta inválida. Digite Sim ou Não.')

    if pergunta in ['N', 'NAO', 'NÃO']:
        break

    valores.sort(reverse=True)

if 5 in valores:
    print('O 5 esta na lista!')

else:
    print('O 5 nao esta na lista!')

print(f'{len(valores)} Valores foram digitados na lista!')
print(f'A lista em ordem decrescente fica {valores}')