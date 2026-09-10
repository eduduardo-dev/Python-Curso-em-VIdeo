palavras = (
    "aprender",
    "programar",
    "linguagem",
    "python",
    "curso",
    "estudar",
    "pratica",
    "trabalho",
    "mercado",
    "programador",
    "futuro",
    "sucesso"
)

for palavra in palavras:
    print(f'Na palavra {palavra.upper()}, temos ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
    print()
