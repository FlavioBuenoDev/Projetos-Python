"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

numero = input("Digitar um número inteiro: ")

if numero.isdigit():
    numero = int(numero) % 2
    if numero == 0:
        print("Numero é par")
    else:
        print("Numero é impar")

# hora
    def hora(horario):
        if horario in range(0, 11):
            print("Bom dia")
        elif horario in range(12, 17):
            print("Boa tarde")
        elif horario in range(18, 23):
            print("Boa tarde")
        else:
            print("Não conheço esse horario !")

    horario = int(input("Digitar a hora: "))
    hora(horario)

    nome = input("Digitar seu nome: ")
    if nome > 1:
        if len(nome) <= 4:
            print("Seu nome é curto")

        elif len(nome) == 5 or len(nome) == 6:
            print("Seu nome é normal")

        else:
            print("Seu nome é muito grande")

    else:
        print("Digite mais de uma letra")


else:
    print("não é um número inteiro")


# Hora


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
