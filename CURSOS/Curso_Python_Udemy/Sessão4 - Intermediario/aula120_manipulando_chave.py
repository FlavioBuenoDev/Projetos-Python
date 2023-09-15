# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

# cria chave dinamica
chave = 'nome'

# acessa a chavee
pessoa[chave] = 'Luiz Otávio'
# cria chave
pessoa['sobrenome'] = 'Miranda'


print(pessoa[chave])

# altera chave
pessoa[chave] = 'Maria'

# exclui a chave
del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))

# Tenta obter uma chave(por padrão retorna none se a chave não existir)
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')
