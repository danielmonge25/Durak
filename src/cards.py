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

    def choice_card(self):
        card = random.choice(self.deck)
        # self.deck.remove(card)
        return card
