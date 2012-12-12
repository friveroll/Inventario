#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pymongo
import codecs
#from Tkinter import *
import ttk
#from inventario import *
import tkFileDialog

from Tkinter import Tk, Menu, Frame, Entry, Label, Text
#from ttk import Frame, Label, Combobox, Entry

class Inventario(Frame):

    def __init__(self, parent):
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Inventario")
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Cerrar", command=self.Close)
        menubar.add_cascade(label="File", menu=fileMenu)




    def Close(self):
        self.parent.destroy()

def main():
  
    root = Tk()
    mainframe = Inventario(root)
    root.geometry("600x300+100+100")
    root.mainloop()  


if __name__ == '__main__':
    main()  