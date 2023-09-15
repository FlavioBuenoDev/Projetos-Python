"""
Iterando strings com while
"""
#       012345678910
"""
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])
"""
nome = 'Flávio Bueno'
# nova_string += '*L*u*i*z* *O*t*á*v*i*o'

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f' * {letra}'
    indice += 1

print(novo_nome)
