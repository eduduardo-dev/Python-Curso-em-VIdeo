valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))

Escolha = 0

while Escolha != 5:
    print('     MENU \n'
      '[1] Somar \n'
      '[2] Multiplicar \n'
      '[3] Maior \n'
      '[4] Novos numeros \n'
      '[5] Sair do Programa \n')

    Escolha = int(input('Oque voce deseja fazer? '))

    if Escolha == 1:
        soma = valor1 + valor2
        print(soma)
    elif Escolha == 2:
        multiplicar = valor1 * valor2
        print(multiplicar)
    elif Escolha == 3:
        if valor1 > valor2:
            maior = valor1
            menor = valor2
            print('Maior valor: {}. Menor valor: {}'.format(maior, menor))
        else:
            maior = valor2
            menor = valor1
            print('Maior valor: {}. Menor valor: {}'.format(maior, menor))
    elif Escolha == 4:
        print('Informe os novos valores a serem escolhidos: ')
        valor1 = int(input('Informe o primeiro valor: '))
        valor2 = int(input('Informe o segundo valor: '))
print('Fim do programa')