import os
from tkinter import Tk

from mygui import egrid, lgrid

root = Tk()


# Add Icon to window Titlebar (2024) rev
if os.name == 'nt':
    homepath = os.path.expanduser('~')
    tempFile = os.path.join(homepath, 'Caveman Software', 'Icon', 'icon.ico')

    if (os.path.exists(tempFile) == True):
        root.wm_iconbitmap(default=tempFile)

    else:
        import create_icon
        print('File Created')
        root.wm_iconbitmap(default=tempFile)


# Add Title from Filename

title = (os.path.basename(__file__)[0:-3])
root.title(title.title())

root.minsize(300, 100)
lgrid(root, 'Label placed in grid 0,0', 0, 0)
lgrid(root, 'Label placed in grid 0,1', 0, 1)
egrid(root, 1, 0)
root.mainloop()
