valores = [[], []]
num = 0

for c in range(1, 8):
    num = (int(input(f'Digite o {c}º valor: ')))

    if num % 2 == 0:
        valores[0].append(num)

    else:
        valores[1].append(num)

valores[0].sort()
valores[1].sort()

print(f'Os valores pares foram {valores[0]}.')
print(f'Enquanto os valores impares foram {valores[1]}.')
