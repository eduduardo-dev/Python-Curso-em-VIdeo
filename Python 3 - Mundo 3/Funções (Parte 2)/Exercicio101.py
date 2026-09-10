def voto():
    from datetime import date


    ano_atual = date.today().year
    idade = ano_atual - int(input('Ano de nascimento: '))
    if idade < 16:
        return  f'Por ter {idade} anos voce tem o voto negado'
    elif 16 <= idade < 18 or idade > 65:
        return f'Por voce ter {idade} anos voce tem o voto opcional'
    else:
        return f'Por voce ter {idade} anos voce tem o voto obrigatorio'

print(voto())