num = int(input('Informe um numero inteiro: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[m O numero {} foi dividido {}'.format(num, total))
if total == 2:
    print('Por isso {} é um numero PRIMO'.format(num))
else:
    print('Por isso {} nao é um numero PRIMO'.format(num))