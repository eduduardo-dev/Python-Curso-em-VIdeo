frase = input('Digite uma frase qualquer: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Palindromo')
else:
    print('Não é Palindromo')


#             isso é oque eu faria:

# frase = input('Digite uma frase: ').strip().upper()
# junto = ''.join(frase.split())
#
# if junto == junto[::-1]:
#     print('Palindromo')
# else:
#     print('Não é Palindromo')