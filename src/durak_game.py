from logging import root
import random
from visual import Visual
from cards import Cards

class Durak_game:
    def run(self):
        self.get_first_player()
        self.game()

    def get_first_player():
        begin = random.randint(0, 1)
        if begin == 0:
            Visual.begin_player_one()
        else:
            Visual.begin_player_two()

    def game():
        visual = Visual()
        cards = Cards()

        cards.createDeck()
        card = cards.choice_card()
        visual.resize_cards(card)
        visual.show_game()


