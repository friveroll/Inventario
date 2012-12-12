# -*- coding: utf-8 -*-
import sys, os
import pymongo
import codecs
import Tkinter,tkFileDialog

class item(object):
    def __init__(self, nombre, cantidad, foto, comentario):
        self.nombre = nombre
        self.cantidad = cantidad
        self.foto = foto
        self.comentario = comentario


    def getItem(self):
         return {'nombre':self.nombre,
                 'cantidad':self.cantidad,
                 'foto':self.foto, 
                 'comentario':self.comentario}


def getFilename(filename=''):
    root = Tkinter.Tk()
    file = tkFileDialog.askopenfilename(parent=root, filetypes=(("Imagen",
                                        "*.jpg"), ("All files", "*.*")))
    root.destroy()
    return os.path.split(file)[1]

def newItem():
    enc = sys.stdin.encoding
    nombre = raw_input('Nombre: ').decode(enc)
    cantidad = raw_input('Cantidad: ').decode(enc)
    foto = getFilename() #raw_input('Foto: ').decode(enc)
    comentario = raw_input('Comentario: ').decode(enc)
    a = item(nombre, cantidad, foto, comentario)
    return a.getItem()



def main():
    mongodb_uri = 'mongodb://localhost:27017'
    db_name = 'inventario'
    enc = sys.stdin.encoding
    
    try:
        connection = pymongo.Connection(mongodb_uri)
        database = connection[db_name]
    except:
        print('Error: Unable to connect to database.')
        connection = None
    if connection is not None:   	
	continuar = True
	while continuar:
		database.equipo.insert(newItem())
		c = str((raw_input('Otro objeto S/N: ').lower()))
		if c == 'n':
			continuar = False
main()
