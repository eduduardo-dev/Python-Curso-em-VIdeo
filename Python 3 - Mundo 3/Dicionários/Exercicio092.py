from datetime import datetime

INSS = dict()

INSS['nome'] = str(input('Digite seu nome: ')).capitalize()

ano_nasc = int(input('Digite seu ano de nascimento: '))

INSS['idade'] = datetime.now().year - ano_nasc

INSS['CTPS'] = int(input('Digite seu CTPS (0 Não tem): '))
if INSS['CTPS'] != 0:
    INSS['ano_contrato'] = int(input('Ano de contratação: '))
    INSS['salario'] = float(input('Salario: R$ '))
    INSS['aposentadoria'] = INSS['idade'] + ((INSS['ano_contrato'] + 35) -  datetime.now().year)

for k, v in INSS.items():
    print(f' - {k} tem o valor {v}')
