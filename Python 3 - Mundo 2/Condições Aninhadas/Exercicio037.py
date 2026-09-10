num = int(input('Digite um valor: '))

print('''Escolha uma das bases para conversão
[ 1 ] para converter para BINARIO
[ 2 ] para converter para OCTAL
[ 3 ] para converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido em BINARIO é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido em OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido em HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida. Tente novamente')