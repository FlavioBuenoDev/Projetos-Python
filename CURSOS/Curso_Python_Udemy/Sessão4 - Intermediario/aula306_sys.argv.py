# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code

import sys

#print(sys.argv)  # Mostra todos os argumentos passados na linha de comando

argumetos = sys.argv
qtd_argumentos = len(argumetos)

if qtd_argumentos < 1:
    print("Você não tem arqgumentos")
else:
    print(f"Você passou os argumetos {argumetos[1:]}")