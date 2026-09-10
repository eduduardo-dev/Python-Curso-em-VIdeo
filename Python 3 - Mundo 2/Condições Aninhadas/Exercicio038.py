num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1 > num2:
    print('O primeiro valor {} é maior que o segundo valor {}'.format(num1, num2))
elif num1 < num2:
    print('O segundo valor {} é maior que o primeiro valor {}'.format(num2, num1))
else:
    print('Os valores {} e {} sao iguais'.format(num1, num2))