from pathlib import Path
from shutil import rmtree

caminho_projeto = Path()
# print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

# Pegar o caminho SRC
print(caminho_arquivo.parent)

# pegar a pasta mae
print(caminho_arquivo.parent.parent)

# Criando caminhos
ideias = caminho_arquivo.parent / 'ideias'
print(ideias)

# Pegar a partir da Home do sistema
arquivo = Path.home() / 'Desktop' / 'arquivo.txt'

# # caso queira salvar o arquivo que esta na memoria
caminho_arquivo.touch()
# # caso queira escrever nesse arquivo
# # Metodo 1
caminho_arquivo.write_text('Ola mundo')
# print(arquivo.read_text)
caminho_arquivo.unlink()
# Metodo 2
# caminho_arquivo.write_text('')
# with caminho_arquivo.open('a+') as file:
#     file.write('Uma linha \n')
#     file.write('Outra linha \n')
# caso queira apagar o arquivo apos o uso
# arquivo.unlink()

# print(caminho_arquivo.read_text())

# criando um diretorio
caminho_pasta = Path.home() / 'Desktop' / 'Python e legal'
caminho_pasta.mkdir(exist_ok=True)
# criar subpastas
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

 
# caso queira criar um arquivo dentro da subpasta
outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Esta na subpasta') 

outro_arquivo = subpasta / 'arquivo2.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Esta na subpasta')

# Apagar pasta
# caminho_pasta.rmdir()

# criar um range de arquivos 
files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'files_{i}.txt'
    file.touch()
    # verifica se o arquivo existir
    if file.exists():
        #apaga o arquivo
        file.unlink()
    else:
        # se ele não existir, criamos o arquivo
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Olá mundo\n')
        text_file.write(f'file_{i}.txt')
    
# apagando recursiva
# rmtree(caminho_pasta)


def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree(file, False)
            file.rmtdir()
        else:
            print('File: ', file)
            file.unlink()
    # if remove_root:
    #     root.rmdir()

rmtree(caminho_pasta)
  