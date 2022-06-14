import random

from visual import Visual

class Durak_game:
    def get_first_player():
        begin = random.randint(0, 1)
        if begin == 0:
            Visual.begin_player_one()
        else:
            Visual.begin_player_two()
