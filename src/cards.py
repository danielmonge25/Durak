import random

class Cards:
    def __init__(self):
        # Definicion del mazo
        self.suits = ["diamonds", "clubs", "hearts", "spades"]
        self.values = range(2, 15) #11=J 12=Q 13=K 14=A

        self.deck = []

    def createDeck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append(f'{value}_of_{suit}')
        #print(self.deck)
        #print(len(self.deck))

    def deal_cards(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

    def choice_card(self, player):
        if (player == 0): # Jugador 1 (Atacante)
            card = random.choice(self.deck_player_one)
            self.deck_player_one.remove(card)
        elif (player == 1): # Jugador 2 (Defensor)
            card = random.choice(self.deck_player_two)
            self.deck_player_two.remove(card)

        return card

    def save_number_card(self, card, player):
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


       
