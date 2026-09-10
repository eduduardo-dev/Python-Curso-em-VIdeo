# valores = list()
# for c in range(1, 6):
#     valores.append(int(input(f'Digite o {c}º valor: ')))
# print(f'O maior valor foi {max(valores)} na posição ', end='')
# for v, c in enumerate(valores):
#     if c == max(valores):
#         print(f'{v}.. ', end='')
# print()
# print(f'E o menor valor foi {min(valores)} na posição ', end='')
# for v, c in enumerate(valores):
#     if c == min(valores):
#         print(f'{v}.. ', end='')
# print()

valores = []

for contador in range(1, 6):
    valor = int(input(f'Digite o {contador}º valor: '))
    valores.append(valor)

maior = max(valores)
menor = min(valores)

print(f'O maior valor foi {maior} na posição ', end='')

for posicao, valor in enumerate(valores):
    if valor == maior:
        print(f'{posicao}.. ', end='')

print()

print(f'E o menor valor foi {menor} na posição ', end='')

for posicao, valor in enumerate(valores):
    if valor == menor:
        print(f'{posicao}.. ', end='')

print()