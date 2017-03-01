# -*- encoding: utf-8 -*-

# Aplikacija, ki odpre okno, ter vanj postavi dva guma in števec

from tkinter import *


class semafor():
    def __init__(self, master):
        '''V okno master postavi dva gumba in števec.'''

        # Stanje števca je na začetku 0
        self.platno = Canvas(master)
        self.platno.pack(side=BOTTOM)

        # Najprej naredimo grafični element Frame, ki služi kot
        # "kontejner", v katerega postavimo gumbe in napise
        frame = Frame(master) # Ta okvir je vsebovan v master-ju
        frame.pack()          # To dejansko naredi vsebino vidno

        gumb_rdeca = Button(frame, text="Rdeča", command=self.rdeca, activebackground="red")
        gumb_rdeca.grid(row=0,column=0)

        gumb_rumena = Button(frame, text="Rumena", command=self.rumena, activebackground="yellow")
        gumb_rumena.grid(row=0,column=1)

        gumb_zelena = Button(frame, text="Zelena", command=self.zelena, activebackground="green")
        gumb_zelena.grid(row=0,column=2)


    def rdeca(self):
            self.platno.config(background="red")

    def rumena(self):
            self.platno.config(background="yellow")

    def zelena(self):
            self.platno.config(background="green")


# Naredimo glavno okno
root = Tk()

aplikacija = semafor(root)

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()
