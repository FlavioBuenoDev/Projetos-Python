# csv.Writer e csv.DictWriter
# csv.reader lê o CSV em formato de lista
# csv.DictWriter escreve o CSV em formato de dicionário

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / "aula294.csv"

lista_clientes = [
    {'Nome': 'Flavio Bueno', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]
# lista_clientes = [
#         ['Flavio Bueno', 'Av 1, 22'],
#         ['João Silva', 'R. 2, "1"'],
#         ['Maria Sol', 'Av B, 3A'],
# ]

with open(CAMINHO_CSV, 'w', encoding="utf8") as arquivo:
    nome_colunas = lista_clientes[0].keys()
    for coluna in nome_colunas:
        print(coluna)

    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
        )
    escritor.writeheader()

    for cliente in lista_clientes:
        # print(cliente)
        escritor.writerow(cliente)

#     for cliente in lista_clientes:       
#         escritor.writerow(cliente)


