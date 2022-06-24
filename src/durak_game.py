import random

from visual import Visual
from cards import Cards
from player import player

class Durak_game:
    def __init__(self):
      self.first_player = 0 # Selecciona el jugador que se va a empezar

    def run(self):
        self.first_player = self.get_first_player()
        self.game(self)

    def get_first_player():
        begin = random.randint(0, 1)
        if begin == 0:
            Visual.begin_player_one()
            return begin
        else:
            Visual.begin_player_two()
            return begin

    def game(self):
        visual = Visual()
        cards = Cards()

        # Nuevo
        player_one = player()
        player_two = player()
        
        cards.createDeck()

        self.draw(self, cards, visual, player_one, player_two)
        
        while (len(cards.deck) != 0) and (len(cards.deck_player_one) != 0) or (len(cards.deck_player_two) != 0):

            self.draw(self, cards, visual, player_one, player_two)

            self.verify_movement(cards, visual)
            visual.clean_old_cards()

    def verify_movement(cards, visual):
        if cards.score_player_one < cards.score_player_two:
            visual.player_defend()   

    def draw(self, cards, visual,  player_one, player_two):
        if (len(cards.deck_player_one) == 0) or (len(cards.deck_player_two) == 0) and len(cards.deck) > 12:
            for index in range(6*2):
                if (index <= 5):
                    card = cards.deal_cards()
                    player_one.append_card(card)
                else:
                    card = cards.deal_cards()
                    player_two.append_card(card)
        elif (len(cards.deck_player_one) == 0) or (len(cards.deck_player_two) == 0) and len(cards.deck) < 12:
             for index in range(2*2):
                if (index <= 2):
                    card = cards.deal_cards()
                    player_one.append_card(card)
                else:
                    card = cards.deal_cards()
                    player_two.append_card(card)
    
        if (player_one.get_size_hand() == 6):
           visual.config_image(player_one.get_hand(), player_two.get_hand())
        
        visual.show_game()
        """if (len(cards.deck_player_one) == 0) or (len(cards.deck_player_two) == 0) and len(cards.deck) > 12:
            cards.deal_cards(6)
        elif (len(cards.deck_player_one) == 0) or (len(cards.deck_player_two) == 0) and len(cards.deck) < 12:
            cards.deal_cards(2)

        if (len(cards.deck_player_one) == 6):
            visual.config_image(cards.deck_player_one, cards.deck_player_two)
        
        visual.show_game()

        if (self.first_player == 0): # Jugador 1 (Atacante)
            card = cards.choice_card(self.first_player)
            cards.save_number_card(card, self.first_player)

            card = cards.choice_card(1)
            cards.save_number_card(card, 1)
        elif (self.first_player == 1): # Jugador 2 (Defensor)
            card = cards.choice_card(self.first_player)
            cards.save_number_card(card, self.first_player)

            card = cards.choice_card(0)
            cards.save_number_card(card, 0)"""