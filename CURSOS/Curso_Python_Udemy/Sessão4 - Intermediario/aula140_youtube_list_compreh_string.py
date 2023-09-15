string = 'Flavio Bueno'
numero_de_letras = 5
#  ''.join
# Passa por cada letra e junta o valor na ''
# nova_string = ''.join([letra for letra in string])

# Pegar grupos de 2 ex: Fl av io
# incrementado com join (a cada 5 letras acrecenta um ponto".")
nova_string = '.'.join([
    string[indice:indice + numero_de_letras]
    for indice in range(0, len(string), numero_de_letras)
])

print(string)
print(nova_string)
