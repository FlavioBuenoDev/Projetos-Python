"""
List comprehension - For alinhados

"""
linhas_e_colunas = [
    (x, y)
    # if y == 2 else 'Voce não é 2'  # vai exibir somente os 2 do y

    # multiplicará cada valor de x,y por 1000 se for 2
    if y == 2 else (x, y * 1000)
    for x in range(1, 11)
    for y in range(1, 6)
    if x != 2  # Vai pular o 2 do x
]

print(linhas_e_colunas)
