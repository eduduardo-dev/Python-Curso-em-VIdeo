def leiaDinheiro():
    while True:
        try:
            valor = input('Digite um valor: ').replace(',', '.')
            valor = float(valor)
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO: \"{valor}\" valor invalido!!\033[m')
        else:
            return valor

