# -*- encoding: utf-8 -*-

# Minimalna aplikacija v Tkinter, ki odpre prazno okno.

import tkinter

# Glavnemu oknu rečemo "root" (koren), ker so grafični elementi
# organizirani v drevo, glavno okno pa je koren tega drevesa

# Naredimo glavno okno
root = tkinter.Tk()

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()
