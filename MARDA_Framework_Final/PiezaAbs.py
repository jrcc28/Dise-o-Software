from abc import ABC, abstractmethod


class PiezaAbs(ABC):
	"""
	Clase Pieza abstracta
	"""

	def __init__(self,tipo,color):
		"""
		Constructor de la clase Pieza.
		Parametros:
		Tipo = tipo de pieza definida por el cliente.
		Color = color de la pieza.
		"""
		self.tipo=tipo
		self.color=color


	def get_tipo(self):
		"""
		Metodo que retorna el tipo de pieza.
		"""
		return self.tipo


	def set_tipo(self,tipo):
		"""
		Metodo set para el tipo de pieza.
		"""
		self.tipo=tipo


	def get_color(self):
		"""
		Metodo que retorna el color de la pieza.
		"""
		return self.color


	def set_color(self,color):
		"""
		Metodo set para el color de la pieza.
		"""
		self.color=color

    #def mis_reglas(self):
	#	pass
