# (Parte1) try e except para tratar exceções
# a = 18
# b = 0
# c = a / b


try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha1'[10000])
    c = a / b
    print('Linha2')
except ZeroDivisionError:
    print('Dividiu por 0')

except NameError:
    print('Nome b não esta definido')

except (TypeError, IndexError):
    print('TypeError')

# Exception trata qualquer erro que apresente no código
except Exception:
    print('Erro desconhecido')

print('CONTINUAR')
