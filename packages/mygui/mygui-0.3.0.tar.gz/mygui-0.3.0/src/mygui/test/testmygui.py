from tkinter import Tk

from mygui import bgrid, egrid, lgrid

root = Tk()
root.minsize(300, 100)
lgrid(root, "Label placed in grid 0,0", 0, 0)
lgrid(root, "Label placed in grid 0,1", 0, 1)
bgrid(root, "Buttonpress", 1, 1)
egrid(root, 1, 0)
root.mainloop()
