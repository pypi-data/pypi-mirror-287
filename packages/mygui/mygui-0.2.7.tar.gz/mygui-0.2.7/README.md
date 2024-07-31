
# mygui 0.2.7

# <img src="https://raw.githubusercontent.com/Caveman-Software/mygui/main/Icon.png" width="35" height="35">  Caveman Software® 2024

## lgrid

example:

---

    import os
    from tkinter import Tk

    from mygui import egrid, lgrid

    root = Tk()
    root.minsize(300, 100)
    lgrid(root, 'Label placed in grid 0,0', 0, 0)
    lgrid(root, 'Label placed in grid 0,1', 0, 1)
    egrid(root, 1, 0)
    root.mainloop()
---

## egrid

---

    import os
    from tkinter import Tk,Entry
    from mygui import egrid, lgrid

    root = Tk()
    root.minsize(300, 100)
    egrid(root,0,0)
    root.mainloop()

---
