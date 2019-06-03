from abc import ABC, abstractmethod

class JugadorAbs(ABC):
	def __init__(self,pieza,nombre):
		self.pieza=pieza
		self.nombre=nombre
	
	def set_nombre(self,nombre):
		self.nombre=nombre
	
	def get_nombre(self):
		return nombre
	
	def set_pieza(self, pieza):
		self.pieza=pieza
	
	def get_pieza(self):
		return pieza
	
		