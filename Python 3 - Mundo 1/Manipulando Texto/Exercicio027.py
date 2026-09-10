nome = str(input('Digite seu nome completo: ')).strip().title()

print('Seu nome completo é {}'.format(nome))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('Seu primeiro nome é: {}'.format(nome[:nome.find(' ')]))
print('Seu ultimo nome é: {}'.format(nome[nome.rfind(' ') + 1:]))

# nome = str(input('Digite seu nome completo: ')).strip().title()
# n = nome.split()
# print('Muito prazer em te conhecer!')
# print('Seu primeiro nome é {}'.format(n[0]))
# print('Seu ultimo nome é {}'.format(n[len(n)-1]))