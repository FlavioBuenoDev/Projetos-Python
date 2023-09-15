nomes = ['Luiz', 'Maria', 'Joana', 'Helena', 'Joana', 'Felipe']

# gerou umanova lista, com minusculo
# novos_nomes = [nome.lower() for nome in nomes]

# Somente a primeira letra
# novos_nomes = [nome.title() for nome in nomes]

# altera a lista de nomes para a 1° minuscula e a ultima Maiuscula
novos_nomes = [f'{nome[:-1].lower()}{nome[1].upper()}'
               for nome in nomes]

print(novos_nomes)
