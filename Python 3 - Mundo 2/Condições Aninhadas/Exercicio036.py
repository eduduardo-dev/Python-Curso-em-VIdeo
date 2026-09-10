valor_imovel = float(input('Qual o valor do imovel? R$'))
salario_comprador = float(input('Qual o salario do comprador? R$'))
periodo_financiamento = float(input('Qual o periodo financiamento? R$'))
prestacao = valor_imovel / (periodo_financiamento * 12)
prestacao_minima = salario_comprador * 30 / 100

    #formatando para padrão brasileiro de moeda
valor_imovel_fmt = f'{valor_imovel:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
salario_comprador_fmt = f'{salario_comprador:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
prestacao_fmt = f'{prestacao:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
prestacao_minima_fmt = f'{prestacao_minima:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

print('Para pagar uma casa de R$ {} em {} anos a prestação sera de R$ {}'
      .format(valor_imovel_fmt, periodo_financiamento, prestacao_fmt))

if prestacao <= prestacao_minima:
    print('Parabens!!!! seu financiamento foi aprovado! \n'
          'Com um salario de R$ {} sua prestação fica em R$ {} (dentro do requisito minimo de R$ {}'
          ''.format(salario_comprador_fmt, prestacao_fmt, prestacao_minima_fmt))
else:
    print('Infezlimente seu financiamento foi reprovado '
          'por exceder os requesitos de 30% do salario! \n'
          'seu salario é de R$ {} e seria necessario uma prestação dentro do valor minimo dos 30% de R$ {}'
          .format(salario_comprador_fmt, prestacao_minima_fmt))