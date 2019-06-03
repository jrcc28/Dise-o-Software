from abc import ABC, abstractmethod

class PiezaAbs(ABC):
	def __init__(self,tipo,color):
		self.tipo=tipo
		self.color=color
	
	def get_tipo(self):
		return self.tipo
	
	def set_tipo(self,tipo):
		self.tipo=tipo
				
	def get_color(self):
		return self.color
	
	def set_color(self,color):
		self.color=color

    def mis_reglas(self):
		pass
		
