from abc import ABC, abstractmethod

class JugadorAbs(ABC):
	"""
	Clase Jugador abstracto
	"""

	def __init__(self,pieza,nombre):
		"""Metodo constructor de la clase jugador."""
		self.pieza=pieza
		self.nombre=nombre

	def set_nombre(self,nombre):
		"""Metodo que setea el nombre del jugador."""
		self.nombre=nombre

	def get_nombre(self):
		"""Metodo que retorna nombre del jugador."""
		return self.nombre

	def set_pieza(self, pieza):
		"""Metodo que setea pieza del jugador."""
		self.pieza=pieza

	def get_pieza(self):
		"""Metodo que retorna pieza del jugador."""
		return self.pieza
