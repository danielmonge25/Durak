from tkinter import *
from PIL import Image, ImageTk

class Visual:
    def __init__(self):
        global root
        root = Tk()
        root.title('Durak game')
        root.geometry("1000x500")
        root.configure(background="green")

        frame = Frame(root, bg="green")
        frame.pack(pady=20)

        # Crea imagen para las cartas de los jugadores
        player_one_frame = LabelFrame(frame, text="Jugador 1", bd=0)
        player_one_frame.grid(row=0, column=0, padx=20, ipadx=20)

        """player_two_frame = LabelFrame(frame, text="Jugador 2", bd=0)
        player_two_frame.grid(row=0, column=1, padx=20, ipadx=20)"""

        # Coloca las cartas en la imagen
        self.player_one_label = Label(player_one_frame, text='')
        self.player_one_label.pack(pady=20)

        """player_two_label = Label(player_two_frame, text='')
        player_two_label.pack(pady=20)"""

        

    def begin_player_one():
        print("Inicia el jugador 1")

    def begin_player_two():
        print("Inicia el jugador 2")

    def show_game(self):
        root.mainloop()

    def resize_cards(self, card):
        global card_image_final 
        card_image = Image.open(f'../cards/{card}.png')
        card_resize_image = card_image.resize((150, 220))
        card_image_final = ImageTk.PhotoImage(card_resize_image)
        self.player_one_label.config(image=card_image_final)