
import random

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Flavio', 'Maria', 'Helena', 'Joana']
# random.shuffle(nomes)
# print(nomes)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
# novos_nomes = random.sample(nomes, k=3)
# print(nomes)
# print(novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
# novos_nomes = random.choices(nomes, k=3)
# print(nomes)
# print(novos_nomes)

# # random.choice(Iterável) -> Escolhe um elemento do iterável
print(random.choice(nomes))