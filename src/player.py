class player:
    def __init__(self):
        self.hand = []

    def append_card(self, card):
        self.hand.append(card)
    
    def get_size_hand(self):
        return len(self.hand)
    
    def get_hand(self):
        return self.hand