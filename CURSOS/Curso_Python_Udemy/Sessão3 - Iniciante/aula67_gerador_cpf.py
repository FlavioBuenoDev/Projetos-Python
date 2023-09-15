'''
    Gerador de CPF
'''

import random
import sys
nove_digitos = ''
# numero aleatório entre 0 e 9
# print(random.randint(0, 9))

for i in range(9):
    # concatena nos 9 digitos pega um numero randomico
    # Obs: não pode esqeucer de converter int para str, pois são dados completamente diferentes
    nove_digitos += str(random.randint(0, 9))

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

dez_digitos = nove_digitos[:9] + str(digito_1)

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

print(cpf_gerado_pelo_calculo)
