# Exercícios com funções


# print(1*2*3*4)

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicacao = multiplicar(10, 2, 3, 4, 5)
print(multiplicacao)

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos


def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é Par'
    return f'{numero} é Impar'


print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))


# Retorne o total para uma variável e mostre o valor
# da variável.
