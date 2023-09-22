# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

from functools import partial

class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__exemplo = 'Isso é private'
        
    def metodo_publico(self):
        return 'Metodo Publico'
    # metodos com undercore não  deve ser utilizado fora da classe
        print(self.__exemplo)

    def _metodo_protected(self):
        return '_metodo_protected'
    
    def __metodo_private(self):
       #print('__metodo private')
        return '__metodo_private'

    
f = Foo()
print(f._metodo_protected())
# não deve sert utilizado dessa foram abaixo
print(f._Foo__metodo_private())
#print(f.public)
#print(f.metodo_publico())
