# Minha logica kkkkk

# valores = []
#
# for contador in range(1, 6):
#     valor = int(input(f'Digite o {contador}º valor: '))
#
#     if not valores:
#         valores.append(valor)
#
#     else:
#         adicionado = False
#
#         for posicao, valor_lista in enumerate(valores):
#             if valor < valor_lista:
#                 valores.insert(posicao, valor)
#                 adicionado = True
#                 break
#
#         if not adicionado:
#             valores.append(valor)
#
# print(valores)

# logica de um mano nos comentarios
# numeros = []
#
# for i in range(5):
#     valor = int(input(f'Digite o {i+1}º valor: '))
#     pos = 0
#     while pos < len(numeros) and valor > numeros[pos]:
#         pos += 1
#     numeros.insert(pos, valor)
# print(f'Os valores digitados em ordem crescente são {numeros}')

# logica do professor
lista = []

for c in range(5):
    valor = int(input(f'Digite o {c+1}º valor: '))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado ao final da lista!')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'Adicionado na posição {pos} da lista!')
                break
            pos += 1
print(f'Os valores digitados em ordem crescente são {lista}')