# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print ("Selecione o número da operção desejada: ")
print ("1 - Soma")
print ("2 - Subtração")
print ("3 - Multiplicação")
print ("4 - Divisão")

sl = int(input("Digite sua opção (1/2/3/4):  "))

def calcular(sl):
    n1 = int(input("Digite o 1° numero:  "))
    n2 = int(input("Digite o 2° numero: "))
    if sl == 1:
        soma = n1 + n2
        print("Resultado: ", soma)
    elif sl == 2:
        sub = n1 - n2
        print("Resultado: ", sub)
    elif sl == 3:
        mult = n1 * n2
        print("Resultado: ", mult)
    elif sl == 4:
        div = n1 / n2
        print("Resultado: ", div)
    else:
        print("Opção Invalida")
        
calcular(sl)