"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


# Argumentos posicional (não nomeados)
soma(1, 2, 3)

# Argumentos nomeados
soma(1, y=2, z=5)

# sep serve para separar os resultados
print(1, 2, 3, sep='-')
