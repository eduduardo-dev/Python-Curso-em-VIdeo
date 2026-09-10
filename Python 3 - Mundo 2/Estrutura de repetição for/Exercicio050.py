soma = 0
for c in range(1, 6 + 1):
    num = int(input('Informe o {}º valor inteiro: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
print(soma)