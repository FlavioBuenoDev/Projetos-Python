""" Calculadora com while """


while True:
    numero_1 = input('Digite um numero : ')
    numero_2 = input('Digite outro numero : ')
    operador = input('Digite o operador (+ - / *): ')

    num_1_float = 0
    num_2_float = 0
    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos numeros digitados são invalidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador invalidos.')
        continue

    if len(operador) > 1:
        print('Digite apenas um Operador.')
        continue

    print('Realizando dua conta. Confira o resultado abaixo:')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = ', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = ', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = ', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = ', num_1_float * num_2_float)
    else:
        print("Nunca deveria chegar aqui")

    sair = input('Quer [s]air ? ').lower().startswith('s')
    print(sair)

    if sair is True:
        break
