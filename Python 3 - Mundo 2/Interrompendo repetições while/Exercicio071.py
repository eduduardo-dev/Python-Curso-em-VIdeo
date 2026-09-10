print('Banco CVV')

valorasacar = int(input('Qual o valor que voce deseja sacar? '))

while True:
    qntnotasde50 = valorasacar // 50
    sobrade50 = valorasacar % 50

    qntnotasde20 = sobrade50 // 20
    sobrade20 = sobrade50 % 20

    qntnotasde10 = sobrade20 // 10
    sobrade10 = sobrade20 % 10

    qntnotasde1 = sobrade10 // 1
    sobrade1 = sobrade10 % 1

    

