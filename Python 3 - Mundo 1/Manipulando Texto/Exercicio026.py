frase = str(input('Digite uma frase: ')).strip().upper()

print('Nessa frase: {}, aparece a letra "A" {} vezes'.format(frase.title(), frase.count('A')))
print('Primeiro na posiçao {} e por ultimo na posição {}'.format(frase.find('A') + 1, frase.rfind('A') + 1))