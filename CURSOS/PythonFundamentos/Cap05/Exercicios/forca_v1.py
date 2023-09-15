# coding
#biblioteca para chamar a palavra de forma randomica
import random

#Board (Tabuleiro)
board = ['''
>>>>>>>>>>>>>>> Hangman <<<<<<<<<<<<<<<<<

 +---+
     |
     |
     |
     |
     |
==========
''','''

 +---+
 |   |
 0   |
     |
     |
     |
==========

''','''

 +---+
 |   |
 0   |
 |   |
     |
     |
==========

''','''

 +---+
 |   |
 0   |
/|   |
     |
     |
==========

''','''

 +---+
 |   |
 0   |
/|\  |
     |
     |
==========

''','''

 +---+
 |   |
 0   |
/|\  |
     |
     |
==========

''','''
 +---+
 |   |
 0   |
/|\  |
/    |
     |
==========

''','''
 +---+
 |   |
 0   |
/|\  |
/ \  |
     |
==========

'''
]
# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        # espera uma palavra
        self.word = word
        # chiação de lista vazia para as letras erradas
        self.missed_letters = []
        # chiação de lista vazia para as letras certas
        self.guessed_letters = []

    # Método para adivinhar a letra
    def guess(self, letter):
    # se(if) a letra dentro(in) da palavra e(and) letra não estiver(not in) dentro da "palavras certas"(guessed_letters)
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
    #se então(elif) a letra não estiver(not in) na palavra e nõa estiver na lista de "palavras erradas", adicione(append)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def hangman_over(self):
       # retorna o hangman_won e o usuário venceu OU verifica se o comprimento das letras erradas for igual a 6
        return self.hangman_won() or (len(self.missed_letters == 6))

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False

    # Método para não mostrar a letra no board
    def hide_word(self):
        # defino o objeto com espaço vazio
        rtn = ''
        # faz um loop for para cada letra dentro da palavra
        for letter in self.word:
        #Se a letra não estiver dentro "palavras certas"
            if letter not in self.guessed_letters:
                # acrescenta _
                rtn += '-'
            else:
                # se não adiciona letra
                rtn += letter
        return rtn

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        # board lista, pode ser acessado cada posição da lista, e utilizamos a marcação de slice(fatia)
        #para ao inves de ficar colocando o indice da lista, utilizamdo o len, que pega o comprimento da lista, ou seja, quando a lista estiver vazia
        #ele trará a primeira posição e assim sucessivamente
        print(board[len(self.missed_letters)])
        #na sequencia, imprimimos na tela palavra, e chamamos hide_word
        print('\nPalavra: ' +self.hide_word())
        print('\nLetras erradas: ',)
        # o for, vai em cada letra, na lista de letras erradas, imprimir a lista
        for letter in self.missed_letters:
            print(letter,)
        print()
        # o for, vai em cada letra, na lista de letras corretas, imprimir a lista
        print('Letras Corretas: ',)
        for letter in self.guessed_letters:
            print(letter,)
        print()
# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

#Função main - Execução do Programa
def main():
    #Objeto
    game = Hangman(rand_word())

    #Enquanto o jogo não estiver terminado, prit do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        user_input = input('\nDigite uma letra: ')
        game.guess(user_input)

    #Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns ! Você Venceu! ')
    else:
        print('\nGame Over ! Você Perdeu')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você ! Agora vá estudar! \n')
# Exescuta o programa
if __name__=="__main__":
    main()