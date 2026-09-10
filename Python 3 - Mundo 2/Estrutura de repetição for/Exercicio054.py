from datetime import date

ano_atual = date.today().year

maioridade = 0
menoridade = 0

for c in range(1, 7 + 1):
    ano = int(input('Digite o ano de nascimento: '))
    idade = ano_atual - ano

    if idade >= 18:
        maioridade = maioridade + 1
    else:
        menoridade = menoridade + 1

print('{} pessoas são maiores de idade'.format(maioridade))
print('{} pessoas são menores de idade'.format(menoridade))