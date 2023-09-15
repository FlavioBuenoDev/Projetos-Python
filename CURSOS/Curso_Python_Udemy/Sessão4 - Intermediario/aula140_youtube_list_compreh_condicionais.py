numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nova lista
novos_numeros = [numero for numero in numeros if numero > 5]
# somente numeros impar
impares = [numero for numero in numeros if numero % 2 != 0]
# somente numeros par
pares = [numero for numero in numeros if numero % 2 == 0]
#
outro_if = [
    numero
    if numero != 6 else 600
    for numero in numeros
    if numero % 2 == 0
]  # [2, 4, 600, 8, 10]

print(numeros)
print(novos_numeros)
print(impares)
print(pares)
print(outro_if)
