primeiro_numero = input('Digite um valor: ')
segundo_numero = input('Digite outro valor: ')

if primeiro_numero > segundo_numero:
    print(f'{primeiro_numero} é maior do que {segundo_numero}')
elif primeiro_numero == segundo_numero or segundo_numero == primeiro_numero:
    print('os valores são igual')
else:
    print(f'{segundo_numero} é maior do que {primeiro_numero}')
