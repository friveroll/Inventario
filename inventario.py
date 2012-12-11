import sys
import pymongo

class item(object):
	def __init__(self, categoria, nombre, cantidad, foto, comentario):
		self.categoria = categoria
		self.nombre = nombre
		self.cantidad = cantidad
		self.foto = foto
		self.comentario = comentario

	def getItem(self):
		return {'categoria':self.categoria, 
		        'nombre':self.nombre, 
		        'cantidad':self.cantidad, 
		        'foto':self.foto, 
		        'comentario':self.comentario}

def main():
    mongodb_uri = 'mongodb://localhost:27017'
    db_name = 'inventario'
    try:
        connection = pymongo.Connection(mongodb_uri)
        database = connection[db_name]
    except:
        print('Error: Unable to connect to database.')
        connection = None
    if connection is not None:   	
	continuar = True
	while continuar:
		categoria = str(raw_input('Categoria: '))
		nombre = str(raw_input('Nombre: '))
		cantidad = int(raw_input('Cantidad: '))
		foto = str(raw_input('Foto: '))
		comentario = str(raw_input('Comentario: '))
		a = item(categoria, nombre, cantidad, foto, comentario)
		database.equipo.insert(a.getItem())
		c = str(raw_input('Añadir otro objeto S/N: ')).lower()
		if c == 'n':
			continuar = False
main()


