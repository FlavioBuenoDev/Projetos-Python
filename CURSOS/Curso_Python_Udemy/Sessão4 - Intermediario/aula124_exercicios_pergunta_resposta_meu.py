# Exercício - sistema de perguntas e respostas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2 ?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5 ?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2 ?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

count_certo = 0

for pergunta in perguntas:
    perguntas = print(pergunta['Pergunta'])
    opcoes = pergunta['Opções']
    resposta_correta = pergunta['Resposta']
    qtd_opcoes = len(pergunta['Opções'])

    for indice, opc in enumerate(opcoes):
        print(indice, ") ", opc)
    print(qtd_opcoes)
    escolha = int(input("Escolha uma opção: "))

    if opcoes[escolha] == resposta_correta:
        print("Você acertou !")
        count_certo += 1

    else:
        print("Você errou !")

print(f"Você acertou {count_certo} de {len(pergunta['Pergunta'])} perguntas")
