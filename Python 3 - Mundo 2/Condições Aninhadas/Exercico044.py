preco_normal = float(input('Qual o preço do produto? R$ '))

print('''Escolha uma forma de pagamento:
[ 1 ] Dinheiro ou cheque
[ 2 ] Cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Sua opção: '))

def moeda(valor):
    return f'R$ {valor:,.2f} reais'.replace(',', 'X').replace('.', ',').replace('X', '.')

if opcao == 1:
    desconto10 = preco_normal - (preco_normal * 0.10)
    print('Por ser pagamento via dinheiro ou cheque. Você recebeu um desconto de 10%'
          ' o preço do produto passa a ser {}'
          .format(moeda(desconto10)))

elif opcao == 2:
    desconto5 = preco_normal - (preco_normal * 0.05)
    print('Por ser pagamento via cartão. Você recebeu um desconto de 5%'
          ' o preço do produto passa a ser {}'
          .format(moeda(desconto5)))

elif opcao == 3:
    print('Por ser pagamento em 2x no cartão. O preço do produto mantem o mesmo valor {}'.format(moeda(preco_normal)))

elif opcao == 4:
    juros = preco_normal + (preco_normal * 0.20)
    print('Por ser pagamento em 3x ou mais no cartão. Você irá pagar 20% de juros'
          ' o preço do produto passa a ser {}'
          .format(moeda(juros)))

else:
    print('Opção invalida. Tente novamente')