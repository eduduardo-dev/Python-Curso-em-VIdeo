def notas(*notes, situation=False):
    """
    -> Função para analisar notas e a situação de varios alunos
    :param notes: uma ou mais notas dos alunos
    :param situation: valor opcional, indicando se deve ou não adcionar a situação
    :return: dicionario com varias informações sobre a situação dos alunos
    """
    resultado = dict()

    resultado['total'] = len(notes)
    resultado['maior'] = max(notes)
    resultado['menor'] = min(notes)
    resultado['media'] = sum(notes) / len(notes)

    if situation:
        if resultado['media'] >= 7:
            resultado['sit'] = 'Aprovado'

        elif resultado['media'] >= 5:
            resultado['sit'] = 'Recuperação'

        else:
            resultado['sit'] = 'Reprovado'

    return resultado


resp = notas(5, 10, 5, 10, situation=True)
print(resp)