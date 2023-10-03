# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
    #yield faz com que a funcao se torne uma generator
        yield arquivo

    except Exception as e:
        print('ocorreu erro', e)
    finally:
        print('Fechando Arquivo')
        arquivo.close()


with my_open('aula242.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)