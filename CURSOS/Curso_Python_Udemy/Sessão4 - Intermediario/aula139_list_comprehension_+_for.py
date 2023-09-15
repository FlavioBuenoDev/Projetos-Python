"""
        list compehesion com mais de 1 for
        
"""

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))


lista = [
    # primeiro x é incluido na lista nova
    # lado esquerdo do for é usado para o mapeamento
    (x, y)
    for x in range(3)
    for y in range(3)

]


lista = [
    # NEsse casso abaixo, para cada x esta gerando uma nova list conprehension
    [(x, letra) for letra in 'Flavio']
    for x in range(3)

]
print(lista)
