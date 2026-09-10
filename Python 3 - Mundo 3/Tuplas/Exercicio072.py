cont = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco',
        'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
        'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
        'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente... ', end='')
print(f'O numero por extenso é {cont[numero]}')