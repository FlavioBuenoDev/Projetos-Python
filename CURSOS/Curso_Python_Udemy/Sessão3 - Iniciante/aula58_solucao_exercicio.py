""""
 Solução exercicios versão professor

"""
import os

# lista vazia
lista = []

# percorre enquanto for verdadeiro
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    # a opção verifica se escolheu inserir
    if opcao == 'i':
        # Limpa a tela
        os.system('clear')
        # Solicita valor
        valor = input('Valor: ')
        # adiciona valor a lista
        lista.append(valor)

    # opção apagar
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )
        try:
            # escolhe um indice para apagar
            indice = int(indice_str)
            # deleta da lista o indice enviado
            del lista[indice]
        # verifica se foi digitado numeros
        except ValueError:
            print('Por favor digite número int.')
        # verifica se o indice na lista
        except IndexError:
            print('Índice não existe na lista')
        # caso não ocorra nenhum dos problemas acima, mas ainda assim ocorra um problema
        except Exception:
            print('Erro desconhecido')
        # listar
    elif opcao == 'l':
        # limpa o terminal
        os.system('clear')
        # Verifica se a lista esiver vazia e imprime a mensagem
        if len(lista) == 0:
            print('Nada para listar')

        # percorre o indice, enumera a lista e imprime valor
        for i, valor in enumerate(lista):
            print(i, valor)

        # caso a escolha não seja desejada, cai no else.
    else:
        print('Por favor, escolha i, a ou l.')
