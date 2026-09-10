listagem = (
    "Lápis", 1.50,
    "Borracha", 2.00,
    "Caderno", 15.90,
    "Caneta", 2.50,
    "Estojo", 25.00,
    "Transferidor", 4.20,
    "Compasso", 9.99,
    "Mochila", 120.32,
    "Livro", 34.90
)

print('-'*30)
print('      Listagem de preço')
print('-'*30)
for i in range(0, len(listagem), 2):
    print(f'{listagem[i]:<20}', end='')
    print(f'R$ {listagem[i + 1]:<20.2f}')
