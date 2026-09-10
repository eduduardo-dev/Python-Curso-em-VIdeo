peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print('Abaixo do peso normal!')
elif IMC < 25:
    print('Peso ideal!')
elif IMC < 30:
    print('Sobrepeso')
elif IMC < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')