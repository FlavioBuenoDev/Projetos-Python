"""
    Expressão regular
"""

import re
import sys

'''cpf_enviado_pelo_usuario = '123.456.789-09' \
    .replace('.', '') \
    .replace('-', '')'''

'''
    Parametros = 
    r = expressão regular
    ^ = negação, ou seja, substituir tudo que não seja um numero
    '' = terceiro parametro é para o que quer substituir
    por ultimo o valor a substituir
'''
entrada = input("Digite seu cpf: ")

cpf_enviado_pelo_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)
# Verificando se o usuário mandou somente letras repetidas
# podemos fazer isso verificando o primeiro caractere da entrada x o tamanho da entrada
entrada_e_sequencial = entrada == entrada[0] * len(entrada)

""" 
    o Python tem uma biblioteca que fecha o código caso o usuário utilize uma entrada errada.
    import sys
    sys.exit()
"""

if entrada_e_sequencial:
    print("Você enviou dados sequencial")
    sys.exit()

print(cpf_enviado_pelo_usuario)
# criou um fatiamento para os
nove_digitos = cpf_enviado_pelo_usuario[:9]
# print(nove_digitos)
contador_regressivo_1 = 10

# inicia uma variavel resultado para somar o digito + contador regressivo
resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
   # print(resultado_digito_1)

# digito 1 pega o resultado da soma de 'resultado_digito_1', multiplica por 10 e divide por 11 para obter o resto
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
# print(digito_1)

################ Segundo Digito #######################

dez_digitos = cpf_enviado_pelo_usuario[:9] + str(digito_1)

contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

# digito 1 pega o resultado da soma de 'resultado_digito_1', multiplica por 10 e divide por 11 para obter o resto
digito_2 = ((resultado_digito_2 * 10) % 11)
digito_2 if digito_2 <= 9 else 0


# validação do CPF
cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

# verifica se o CPF esta correto
if cpf_enviado_pelo_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_pelo_usuario} é válido')
else:
    print('CPF Invalido')
