# Funçoes decoradoas e decoradores de classes
def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr

def adiciona_repr(cls):
     cls.__repr__= meu_repr
     return cls

# class MyReprMixin:
#      def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr
     
@adiciona_repr   
class Time:
    def __init__(self, nome):
        self.nome = nome

@adiciona_repr   
class Planeta:
    def __init__(self, nome):
        self.nome = nome

# Time = adiciona_repr(Time)
brasil = Time('Brasil')
portugal = Time('Portugal')

# Planeta = adiciona_repr(Planeta)
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)
print(terra)
print(marte)

