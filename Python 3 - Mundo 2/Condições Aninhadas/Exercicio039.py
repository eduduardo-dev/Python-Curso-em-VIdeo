from datetime import date

ano_nasc = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
ano_restante = 18 - idade

if idade < 18:
    print('Você ainda não tem que se alistar, pois faltam {} anos'.format(ano_restante))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!!')
elif 18 < idade <= 45:
    print('Você tem {} anos e caso não tenha se alistado ainda, corra para se alistar pois ja passou {} anos'.format(idade, abs(ano_restante)))
