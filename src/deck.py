'''
Creado el 26 de Junio del 2022

@autores: Fernando Aguero, Daniel MOnge, Alejandro Sanchez, Andre Villegas
'''

import random

class deck:
    def __init__(self):
        """
            Constructor de la clase Cards

            Esta funcion no retorna nada
        """

        # Definicion del mazo
        self.suits = ["diamonds", "clubs", "hearts", "spades"]
        self.values = range(2, 15) #11=J 12=Q 13=K 14=A

        self.deck = []

    def get_len_deck(self):
        return len(self.deck)
    
    def get_deck(self):
        return self.deck
    
    def createDeck(self):
        """
            Crea el mazo para el juego

            Esta funcion no retorna nada
        """

        for suit in self.suits:
            for value in self.values:
                self.deck.append(f'{value}_of_{suit}')

    def deal_cards(self):
        """
            Elige una carta del mazo aleatoriamente y la elimina

            Esta funcion retorna una carta del mazo
        """

        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

    def choice_card(self, player):
        """
            No utilizado aun

            Elige una carta de la mano del jugador

            El parametro player debe ser un entero (0 es jugadr 1, 1 es jugador 2)

            Esta funcion retorna una carta del mazo del jugador
        """

        if (player == 0): # Jugador 1 (Atacante)
            card = random.choice(self.deck_player_one)
            self.deck_player_one.remove(card)
        elif (player == 1): # Jugador 2 (Defensor)
            card = random.choice(self.deck_player_two)
            self.deck_player_two.remove(card)

        return card

    def save_number_card(self, card, player):
        """ 
            No utilizado aun
            
            Guarda el numero de la carta para luego comparar y saber quien gana la ronda

            El parametro player debe ser un entero (0 es jugadr 1, 1 es jugador 2)
            El parametro card debe ser un string (Carta a sacar el numero)

            Esta funcion no retorna nada
        """

        digit_card = int(card.split("_", 1)[0]) # Solo se deja el numero con el fin de comparar
        if (player == 0): # Jugador 1 (Atacante)
            if digit_card == 14: # Caso en que la carta es un Ace
                self.score_player_one = 11
            elif digit_card == 11 or digit_card == 12 or digit_card == 13:
                self.score_player_one = 10
            else:
                self.score_player_one = digit_card
        elif (player == 0): # Jugador 2 (Defensor)
            if digit_card == 14: # Caso en que la carta es un Ace
                self.score_player_two = 11
            elif digit_card == 11 or digit_card == 12 or digit_card == 13:
                self.score_player_two = 10
            else:
                self.score_player_two = digit_card


       
