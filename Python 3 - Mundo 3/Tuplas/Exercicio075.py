valores = tuple(int(input(f'Digite o {c}º valor: '))for c in range(1, 5)) #assim eu nao preciso escrever a pergunta n vezes

if valores.count(9) == 0:
    print('O valor 9 apareceu nenhuma vez')
else:
    print(f'O numero 9 apareceu {valores.count(9)} vezes')

print(f'O valor 3 foi digitado pela primeira vez na {valores.index(3) + 1}º posição'
      if 3 in valores else 'Não foi digitado valor 3')

print('Valores pares digitados foram', end=' ')
print({n for n in valores if n % 2 == 0}, end=' ')