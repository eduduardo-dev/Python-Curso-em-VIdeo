from datetime import date

Ano = int(input('Digite o ano que gostaria de calcular '
                '(Caso queira infromar o ano atual, digite 0): '))

Ano_Bissexto = Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0

if Ano == 0:
    Ano = date.today().year

if Ano_Bissexto:
    print('{} é um ano bissexto!!!'.format(Ano))
else:
    print('{} não é um ano bissexto!!!'.format(Ano))