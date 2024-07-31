
import os

try:

    from mygui import lgrid
except:
    os.system('pip install mygui')
    from mygui import lgrid

from tkinter import Tk

root = Tk()


# Add Title from Filename

title = (os.path.basename(__file__)[0:-3])
root.title(title.title())

root.minsize(300, 100)

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

lgrid(root, 'Label placed in grid 5,5', 5, 5)
lgrid(root, 'Label placed in grid 6,6', 6, 6)

root.mainloop()
