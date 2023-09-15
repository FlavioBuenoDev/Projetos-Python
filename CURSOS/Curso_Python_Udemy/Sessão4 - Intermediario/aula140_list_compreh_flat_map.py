numeros = [[numero, numero ** 2] for numero in range(10)]
# flat serva para achatar o resultado e não ter uma lista dentro de ourta lista
flat = [y for x in numeros for y in x]
print(flat)
