nota1 = float(input('Informe sua primeira nota: '))
nota2 = float(input('Informe sua segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('REPROVADO!!! ja que sua média {:.1f} esta abaixo de 5.0'.format(media))
elif 5.0 <= media <= 6.9:
    print('RECUPERAÇÃO!!! Ja que sua média {:.1f} esta entre 5.0 e 6.9'.format(media))
else:
    print('APROVADO!!! Sua média foi {:.1f} estando acima de 6.9'.format(media))