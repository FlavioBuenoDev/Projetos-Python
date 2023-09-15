#Formatação de strings com o método format
"""
a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'a={0} b={1} c={nome3:.2f}'
# nome3 é chamado de parametro nomeado, ele se torna o parametro e o "C" se torna o argumento
# Obs. Tudo que vier após o paramentro nomeado, tambem tem que ser nomeado
formato = string.format(
    a,b,nome3=c
    )
print(formato)
"""

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))