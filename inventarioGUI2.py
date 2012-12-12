# -*- coding: utf-8 -*-
import sys, os
import pymongo
import codecs
from Tkinter import *
import ttk
#from inventario import *
import tkFileDialog

root = Tk()
root.title('Inventario')

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

categoriavar = StringVar()
nombre = StringVar()
precio = StringVar()
cantidad = StringVar()

comentario = StringVar()

ttk.Label(mainframe, text='Categoria: ').grid(column=1, row=1, sticky=(W, E))
categoria = ttk.Combobox(mainframe, width=20, textvariable=categoriavar)
categoria.grid(column=2, row=1, sticky=(W, E))

categoria['values'] = (u'Quimica', u'Biologia', u'Fisica')

ttk.Label(mainframe, text='Nombre: ').grid(column=1, row=2, sticky=(W, E))
nombre_entry = ttk.Entry(mainframe, width=20, textvariable=nombre)
nombre_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, text='Precio: ').grid(column=1, row=3, sticky=(W, E))
precio_entry = ttk.Entry(mainframe, width=20, textvariable=precio)
precio_entry.grid(column=2, row=3, sticky=(W, E))

ttk.Label(mainframe, text='Cantidad: ').grid(column=1, row=4, sticky=(W, E))
cantidad_entry = ttk.Entry(mainframe, width=20, textvariable=cantidad)
cantidad_entry.grid(column=2, row=4, sticky=(W, E))

class Photo(object):
    def __init__(self, filename):
        self.filename = filename
    
    def getFilename(self):
        file = tkFileDialog.askopenfilename(filetypes=(("Imagen",
                                            "*.jpg"), ("All files", "*.*")))
        if file != None:
            self.filename.set('%s' % os.path.split(file)[1])
    
foto = StringVar("")
photo = Photo(foto)

ttk.Button(mainframe, text='Foto', command=photo.getFilename).grid(column=1, row=5, sticky=(W, E))
foto_entry = ttk.Label(mainframe, width=20,textvariable=foto)
foto_entry.grid(column=2, row=5, sticky=(W, E))


ttk.Label(mainframe, text='Comentario: ').grid(column=1, row=6, sticky=(W, E))
comentario_entry = ttk.Entry(mainframe, width=20, textvariable=comentario)
comentario_entry.grid(column=2, row=6, sticky=(W, E))


def insertDb():
    mongodb_uri = 'mongodb://localhost:27017'
    db_name = 'inventario'
    try:
        connection = pymongo.Connection(mongodb_uri)
        database = connection[db_name]
    except:
        print('Error: Unable to connect to database.')
        connection = None
    if connection is not None:
        database.equipo.insert({'categoria':categoria, 
                                'nombre':nombre_entry,
                                'precio':precio_entry, 
                                'cantidad':cantidad_entry,
                                'foto':foto_entry, 
                                'comentario':comentario_entry})

ttk.Button(mainframe, text='Insertar', command=insertDb).grid(column=2, row=7, sticky=E)


root.mainloop()