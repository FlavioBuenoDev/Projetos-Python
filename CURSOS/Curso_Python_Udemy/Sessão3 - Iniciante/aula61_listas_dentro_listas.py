"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)],  # 2
]

# print(salas[0][1])
print(salas[2][3][3])

for sala in salas:
    for aluno in sala:
        print(aluno)
