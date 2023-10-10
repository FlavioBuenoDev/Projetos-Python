
# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html
from _collections_abc import Iterator, Sequence

class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1
# método especial que retorna o comprimento da lista
    def __len__(self) -> int:
        return self._index
#método especial que permite definir o valor de um elemento em uma posição específica da lista. 
    def __setitem__(self, index, value):
        self._data[index] = value
#método especial que retorna o valor de um elemento em uma posição específica da lista.
    def __getitem__(self, index):
        return self._data[index]

    #Implementando o iterator
    def __iter__(self) -> Iterator:
        return self
    
    def __next__(self):
       # Logica do next
       if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

       value = self._data[self._next_index]
       self._next_index += 1
       return value

#será executado se o script for executado diretamente, não se for importado como um módulo
if __name__ == '__main__':
    lista = MyList()
    lista.append('Maria', 'Helena', 'tiago')
    lista.append('Joao')
    lista[0] = ('Jonas')
    #print(lista._data)

    for item in lista:
        print(item)
    print('---------------')


