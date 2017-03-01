from tkinter import *


class risalnik():
    def __init__(self, master):
        '''V okno master postavi dva gumba in števec.'''

        # Stanje števca je na začetku 0
        self.platno = Canvas(master)
        self.platno.pack(side=BOTTOM)

        # Najprej naredimo grafični element Frame, ki služi kot
        # "kontejner", v katerega postavimo gumbe in napise
        frame = Frame(master) # Ta okvir je vsebovan v master-ju
        frame.pack()          # To dejansko naredi vsebino vidno

        glavni_menu = Menu(master) # Ga uvrti v hierarhijo objektov upor. vmesnika
        master.config(menu=glavni_menu) # Nastavi menu aplikacije

        # Naredimo podmenu "File"
        risalnik_menu = Menu(glavni_menu)
        glavni_menu.add_cascade(label="Risalnik", menu=risalnik_menu)

        risalnik_menu.add_command(label="Počisti")
        risalnik_menu.add_command(label="Končaj", command=master.destroy)

        barva_menu = Menu(glavni_menu)
        glavni_menu.add_cascade(label="Barva", menu=barva_menu)

        barva_menu.add_command(label="Rdeča")
 
        debelina_menu = Menu(glavni_menu)
        glavni_menu.add_cascade(label="Debelina", menu=debelina_menu)

        self.platno.bind("<Button-1>", self.narisi_krogec)
        self.platno.bind("<B1-Motion>", self.narisi_krogec)

    def narisi_krogec(self, event):
        '''Nariši krogec, kjer trenutno stoji miška.'''
        self.platno.line(event.x, event.y)

    def pocisti(self):
        self.platno.delete(ALL)



##        # Dodamo izbire v file_menu
##        file_menu.add_command(label="Izbira 1", command=self.izbira1)
##        file_menu.add_command(label="Izbira 2", command=self.izbira2)
##        file_menu.add_separator() # To doda separator v menu
##        file_menu.add_command(label="Quit", command=master.destroy)
##
##        # Naredimo podemnu "Edit"
##        edit_menu = Menu(glavni_menu)
##        glavni_menu.add_cascade(label="Edit", menu=edit_menu)
##
##        # Dodamo izbire v edit_menu. Te izbire ne delajo ničesar,
##        # ker nismo nastavili command=...
##        edit_menu.add_command(label="My Copy")
##        edit_menu.add_command(label="My Cut")
##        edit_menu.add_command(label="My Paste")
##        edit_menu.add_command(label="My Delete")


# Naredimo glavno okno
root = Tk()

stevec = risalnik(root)

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()
