salario = float(input('Digite o seu salario: '))

if salario >= 1250:
    aumento = salario + (salario * 15 / 100)
    print('Com um aumento de 15% seu salario passa a ser R$ {:.2f} reais'.format(aumento))

else:
    aumento = salario + (salario * 10 / 100)
    print('Com um aumento de 10% seu salario passa a ser R$ {:.2f} reais'.format(aumento))