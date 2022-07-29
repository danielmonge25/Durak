'''
Creado el 26 de Junio del 2022

@autores: Fernando Aguero, Daniel Monge, Alejandro Sanchez, Andre Villegas
'''

import random
from card import Card
from abstract_deck import Abstract_Deck

class deck(Abstract_Deck):
    def __init__(self):
        """
            Constructor de la clase deck

            Esta funcion no retorna nada
        """

        # Definicion del mazo
        self.suits = ["diamonds", "clubs", "hearts", "spades"]
        self.values = range(2, 15) #11=J 12=Q 13=K 14=A

        # Mazo del juego
        self.deck = []

    def createDeck(self):
        """
            Crea el mazo para el juego

            Esta funcion no retorna nada
        """

        """for suit in self.suits:
            for value in self.values:
                self.deck.append(f'{value}_of_{suit}')"""
        
        for suit in self.suits:
            for value in self.values:
                card = Card()
                card.set_card_name(f'{value}_of_{suit}')
                self.deck.append(card)
                #print(card.get_card_name())
                
    def deal_cards(self):
        """
            Elige una carta del mazo aleatoriamente y la elimina

            Esta funcion retorna una carta del mazo
        """

        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

    def get_len_deck(self):
        """
            Esta funcion devuelve el tamanyo del mazo
        """

        return len(self.deck)
    
    def get_deck(self):
        """
            Esta funcion devuelve el mazo del juego
        """

        new_deck = []
        
        #print("MAZO")
        for index in range(len(self.deck)):
            new_deck.append(self.deck[index].get_card_name())
            #print(new_deck[index])
        #print("\n")

        return new_deck