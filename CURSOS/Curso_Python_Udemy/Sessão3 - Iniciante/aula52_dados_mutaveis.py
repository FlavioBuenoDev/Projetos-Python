"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
"""nome = 'Flavio'
noutra_variavel = nome
nome = 'Bueno'


print(noutra_variavel)
print(nome)
"""

lista_a = ['Flavio', 'Bueno', 1, True, 1.2]
lista_b = lista_a.copy()


lista_a[0] = 'Qualquer coisa'
print(lista_a)

print(lista_b)
