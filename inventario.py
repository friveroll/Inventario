import pymongo

class item(object):
	def __init__(self, categoria, nombre, cantidad, foto, comentario):
		self.categoria = categoria
		self.nombre = nombre
		self.cantidad = cantidad
		self.foto = foto
		self.comentario = comentario
		conn = pymongo.Connection()
		db = conn.inventario

	def getItem(self):
		return {'categoria':self.categoria, 'nombre':self.nombre, 'cantidad':self.cantidad, 'foto':self.foto, 'comentario':self.comentario}

	def dbInsert(self):
		return db.insert(getItem())

def main():
	continuar = True
	while continuar:
		categoria = str(raw_input('Categoria: '))
		nombre = str(raw_input('Nombre: '))
		cantidad = int(raw_input('Cantidad: '))
		foto = str(raw_input('Foto: '))
		comentario = str(raw_input('Comentario: '))
		a = item(categoria, nombre, cantidad, foto, comentario)
		a.dbInsert()
		c = str(raw_input('Continuar S/N: ')).lower()
		if c == 'n':
			continuar = False
main()


