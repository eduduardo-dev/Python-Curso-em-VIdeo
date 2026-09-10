expressao = str(input('Digite uma expressão: '))

pilha_parenteses = []

for caractere in expressao:
    if caractere == '(':
        pilha_parenteses.append(caractere)

    elif caractere == ')':
        if len(pilha_parenteses) > 0:
            pilha_parenteses.pop()
        else:
            pilha_parenteses.append(caractere)
            break

if len(pilha_parenteses) == 0:
    print('Expressão VALIDA!!')
else:
    print('Expressão INVALIDA!!')

# expressao = input('Digite uma expressão: ')
#
# parenteses = []
# valido = True
#
# for caractere in expressao:
#     if caractere == '(':
#         parenteses.append(caractere)
#
#     elif caractere == ')':
#         if parenteses:
#             parenteses.pop()
#         else:
#             valido = False
#             break
#
# if parenteses:
#     valido = False
#
# if valido:
#     print('A expressão está correta!')
# else:
#     print('A expressão está incorreta!')