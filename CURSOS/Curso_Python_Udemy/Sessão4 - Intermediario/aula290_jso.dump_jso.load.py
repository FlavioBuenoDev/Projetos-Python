# json.dump e json.load com arquivos

import json
import os

NOME_ARQUIVO = 'Aula290.json'
# pega caminho absoluto
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
       os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
        )
)


filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',

    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

# converter para um dicionario em python
# print(json.loads(string_json))

# criar um arquivo para jogar as informações
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

# abrindo o arquivo e convertendo novamente para json
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    filme_do_json = json.load(arquivo)
    print(filme_do_json)

