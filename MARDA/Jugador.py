from JugadorAbs import JugadorAbs

class Jugador(JugadorAbs):
	def __init__(self,pieza,nombre):
		self.pieza=pieza
		self.nombre=nombre

	def set_nombre(self,nombre):
		self.nombre=nombre


	def get_nombre(self):
		return self.nombre

	def set_pieza(self, pieza):
		self.pieza=pieza

	def get_pieza(self):
		return self.pieza

	

		