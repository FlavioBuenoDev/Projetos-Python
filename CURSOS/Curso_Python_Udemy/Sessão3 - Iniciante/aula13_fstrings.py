nome = 'Flavio Bueno'
peso = 80
altura = 1.73

imc = peso / (altura ** 2)

# f-strings
# adicionadno f a frente da string, possibilita o uso de variaveis dentro da string
# {altura:.2f} - 2f após a altura formata casas decimais
linha1 = f'{nome} tem {altura:.2f} de altura'
linha2 = f'pesa {peso} quilos e seu imc é'
linha3 = f'{imc:.2f}'
print(linha1)
print(linha2)
print(linha3)
