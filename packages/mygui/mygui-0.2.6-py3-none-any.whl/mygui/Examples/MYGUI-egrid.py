import os
from tkinter import Entry, Tk

import create_icon
from mygui import egrid, lgrid

root = Tk()


# Add Title from Filename

title = (os.path.basename(__file__)[0:-3])
root.title(title.title())

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

root.minsize(300, 100)
egrid(root, 0, 0)
root.mainloop()
