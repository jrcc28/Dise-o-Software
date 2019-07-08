from abc import ABC, abstractmethod
"""
Clase jugador abstracto
"""
class JugadorAbs(ABC):
	"""metodo constructor"""
	def __init__(self,pieza,nombre):
		self.pieza=pieza
		self.nombre=nombre
	"""setea el nombre"""
	def set_nombre(self,nombre):
		self.nombre=nombre
	"""retorna nombre"""
	def get_nombre(self):
		return self.nombre
	"""setea pieza"""
	def set_pieza(self, pieza):
		self.pieza=pieza
	"""retorna pieza del jugador"""
	def get_pieza(self):
		return self.pieza
