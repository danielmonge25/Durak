from game import Game

from visual import Visual
from cards import Cards
from player import player

class durak(Game):
   reglas = "El objetivo es descartar todas tus cartas antes que tus oponentes en diferentes rondas de ataque y defensa hasta que no hayan cartas en el mazo.\n Se juega con 36 cartas de la baraja inglesa, de menor a mayor valor: 6 7 8 9 10 J Q K A. \n Antes de empezar se coloca una carta boca arriba (cruzada bajo el mazo) que indicará el palo de «triunfo».A cada jugador se le reparten 6 cartas. Si algún jugador tiene todas la cartas rojas, negras o 5 cartas del mismo palo, se vuelve a repartir.En cada ronda hay un defensor (indicado con un escudo) y tres atacantes.Empieza atacando el jugador que tiene la carta de triunfo más baja en su mano.El jugador a su izquierda es el defensor. \n El atacante juega una carta boca arriba sobre la mesa. El defensor debe responder con una carta superior del mismo palo o una carta del palo de triunfo para no perder la defensa. Se pueden realizar tantos ataques como cartas tiene el defensor hasta un máximo de 6. Para volver a atacar debe haber sobre la mesa una carta del mismo valor. Si un jugador no puede atacar más, pasará el turno al jugador de su izquierda. \nFinal de la ronda \n La ronda finaliza cuando todos los jugadores han tenido oportunidad de atacar o se ha alcanzado el número máximo de ataques. Si el defensor ha tenido éxito, se descartarán todas las cartas de la mesa y será el primero en atacar en la siguiente ronda. Si ha fracasado, deberá robar todas las cartas de la mesa y perderá el turno de atacar en la siguiente ronda. Al acabar la ronda, todos los jugadores deberán robar del mazo hasta tener de nuevo 6 cartas, por orden primero los jugadores atacantes y por último el defensor. \nFinal de la partida\n Gana el primer jugador que no tenga cartas y no haya cartas disponibles para robar.El resto de jugadores seguirán jugando para salvarse de ser el «durak»." 
   
   def play(self):
      visual = Visual(self.reglas)
      cards = Cards()
      player_one = player()
      player_two = player()
      visual.set_reglas(self.reglas)
      # Crea el mazo para el juego
      cards.createDeck()

      visual.pick_turn()

      self.draw(self, cards, visual, player_one, player_two)

      if (player_one.get_size_hand() == 6):
         visual.config_image(player_one.get_hand(), player_two.get_hand())

      visual.show_game()
      
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

   def next_turn(self):
      print("Hola")
      
   def set_rules(self):
      print("Hola2")
      
   def get_state(self):
      print("Hola3")

   def get_card(self):
      print("Hola4")

   def end(self):
      print("Hola5")

   def printReglas(self):
      print(self.reglas)



    
 