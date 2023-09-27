# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.

from abc import ABC, abstractmethod

# AbstractFoo poderia ser AbstractPessoa, Pessoabstract ou seja, poderia ser qualquer coisa que vc queira aqui
# Ela é uma super classe que serve para ser uma classe de ABC
# Ela não é uma classe abstrata, porque não tem nenhum metodo abstrato.
# essa classe não é para ser usada (Ela é como um pensamento da sua cabeça, não existe, vc não pode usar )
class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name
        

    #decorator
    @property
    @abstractmethod
    def name(self):
        ...
        #Modificado após a explicação
        #return self._name

    # @name.setter
    # def name(self, name):
    #     ...
    #     # 2° parte após explicação
    #     '''
    #         Quando eu configurar o setter, eu já configuro uma propriedade qualquer, criei lá na classe abstrata (self._name = None) para a propriedade qualquer,
    #         ja configuro ela aqui(self._name = name) e retorno ela no getter(return self._name)

    #     '''
    #     self._name = name


# essa classe complementa a classe abstractfoo
# essa classe é uma classe concreta, uma clase que deve ser usada, diferente da classe abstrata acima
class Foo(AbstractFoo):
    # esse init sobrepoe o init da classe abstrata, por isso deve existir o super() nessa classe
    def __init__(self, name):
        super().__init__(name)
        # esse init é inutil, ele só repassa as informações para o init da classe AbstractFoo
       # print('Sou Inutil')

    # quando fo rinstanciada essa classe, vai criar uma property
    #@property
    # def name(self):
    #     return self._name
    
    # @name.setter
    # def name(self, name):
    #     self._name = name

    ####################################### Outra forma mais facil seria isso
    name = ''
    
    
"""
Explicação:

criei uma variavel (foo) chamando a classe (Foo), passei o parametro ('Bar') que vai ser carregado na 'name' da classe
que passei para a super().__init__(name) que foi para a init da superclasse( __init__(self, name)) que veio aqui (self.name = name), mas isso é uma property,
quando chamo um sinal de atribuição (=) em uma property, estou chamando o setter dessa property, quando eu fizer isso, ele vai chamar o metodo(@name.setter) dessa property
Como não estou fazendo nada nesse setter, o getter não tem o que retornar, quando eu chamar o getter la embaixo(print(foo.name)), ele vai aparecer 'None'.
Isso foi proposital para entender o código
""" 
foo = Foo('Bar')
print(foo.name)

"""
Uma property é um methodo que se comporta como um atributo
"""