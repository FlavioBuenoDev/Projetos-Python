# Condicionais
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# com filtro numero > 5
novos_numeros = [numero for numero in numeros if numero > 5]

# com filtro para pegar somente os numeros impares
impares = [numero for numero in numeros if numero % 2 != 0]


# lista original
print(numeros)
# novos numeros
print(novos_numeros)

# novos numeros impares
print(impares)
