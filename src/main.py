'''
Creado el 26 de Junio del 2022

@autores: Fernando Aguero, Daniel Monge, Alejandro Sanchez, Andre Villegas
'''

from durak import durak
from visual import Visual
from french_deck import deck
from player import player

def main():
    """
        Metodo principal del programa

        Esta funcion no retorna nada
    """

    cards = deck()

    # Creacion de los jugadores
    player_one = player()
    player_two = player()

    visual = Visual(player_one, player_two)

    durak_game = durak(cards, player_one, player_two, visual)

    visual.set_game(durak_game)

    durak_game.play()

if __name__ == "__main__":
    main()