""""
    fAÇA UMA LISTA DE COMPRAS COM LISTA
    O usuario deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
    Não permita que o programa quebre com erros de indices inexistentes na lista

"""
lista = []
while True:
    valor_permitido = ['i', 'a', 'l']

    selecao = input('Selecione uma opcao: \n [i]nserir [a]pagar [l]listar : ')
    if selecao in valor_permitido:
        if selecao == 'i':
            valor = input("Valor: ")
            lista.append(valor)

        if selecao == 'a':
            indice = int(input('Selecione o indice que deseja excluir: '))
            i = 0
            while i < len(lista):
                if i == indice:
                    lista.pop(indice)
                    print("Indice encontrado e removido")
                    break
                else:
                    print("Indice Não encontrado")
                i += 1

        if selecao == 'l':
            for indice, nome in enumerate(lista):
                print(indice, nome)

    else:
        print("Não é permitido")
