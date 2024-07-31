import os
from tkinter import Tk

from mygui import bgrid, egrid, lgrid

root = Tk()
root.minsize(300, 100)
lgrid(root, 'Label placed in grid 0,0', 0, 0, padx=20, pady=20)
lgrid(root, 'Label placed in grid 0,1', 0, 1)
egrid(root, 1, 0)
bgrid(root, "button", 2, 0, padx=20)
root.mainloop()
