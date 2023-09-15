# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
   print('ABRIR O ARQUIVO')
   8 / 0
   # pode pegar o nome do erro com __class__.__name__
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    # pode ter quantos except quiser
except IndexError:
    print('ERRO DE INDEX')
    # pode ter except que trata mais de uma excessão
except (NameError, ImportError):
    print('erro')
    # caso o codigo ocorra sem erros, cai no else
else:
    print('NÃO DEU ERRO')
    # finally sempre vai funcionar
finally:
    print('FECHAR ARQUIVO')


"""
    lembrando
    try e else não pode vir sozinho, tem que ter pelo menos um except ou finaly

    link das excessoes
    https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

"""
