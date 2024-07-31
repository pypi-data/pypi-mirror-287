# LGRID , EGRID , BGRID

__version__ = "0.3.1"
__author__ = "Michael E Mulvey"
from tkinter import Button, Entry, Label, Tk


def lgrid(self, text, gridcol, gridrow, **kwargs):
    """Label Maker for quick labels in a GUI window.
    Example :
        lgrid(root,'text to enter',0,0)

    Where root is the instance of tkinter ,
    'Text to enter' is just that,
    0,0 is the column and row to place them"""
    lbl = Label(self, text=text, **kwargs)
    lbl.grid(column=gridcol, row=gridrow)


def egrid(self, col, row, **kwargs):
    """Entry Maker for a quick entry in a GUI window.
    Example:
    egrid(root,1,0)
    """
    e1 = Entry(self, **kwargs)
    e1.grid(column=col, row=row)


def bgrid(self, text, col, row, **kwargs):
    """Button Maker for quick entry in a grid"""
    btn1 = Button(self, text=text, **kwargs)
    btn1.grid(column=col, row=row)
