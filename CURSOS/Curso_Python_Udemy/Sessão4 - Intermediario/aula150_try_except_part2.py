# (Parte1) try e except para tratar exceções
# a = 18
# b = 0
# c = a / b

"""
string = 'Flavio'  # instancia da classe str
print(isinstance(string, str))

"""

try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha1'[10000])
    c = a / b
    print('Linha2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)

except NameError:
    print('Nome b não esta definido')
# pega o erro com o as error
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    # Erro da excessao
    print('MSG: ', error)
    # Pega a classe do erro
    print('Nome: ', error.__class__.__name__)


# Exception trata qualquer erro que apresente no código
except Exception:
    print('Erro desconhecido')

print('CONTINUAR')
