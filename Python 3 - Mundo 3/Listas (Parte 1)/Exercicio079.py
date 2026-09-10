valores = []
contador = 1

while True:
    verific = int(input(f'Digite o {contador}º valor: '))
    if verific not in valores:
        valores.append(verific)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar!')

    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break

    contador += 1
valores.sort()
print(valores)