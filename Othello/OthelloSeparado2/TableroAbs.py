from abc import ABC, abstractmethod

class TableroAbs(ABC):
	def __init__(self):
			
		self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 3, 0, 0, 0],
			[0, 0, 0, 1, 2, 3, 0, 0],
			[0, 0, 3, 2, 1, 0, 0, 0],
			[0, 0, 0, 3, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0]]
		self.num_negras=2
		self.num_blancas=2
		#1 es ficha negra
		#2 es ficha blanca
		#si es 3 es que es una posicion valida a poner ficha
		
	def get_num_negras(self):
		pass
	def get_num_blancas(self):
		pass
	def set_negras(self, cantidad):
		print ("holahola")
		pass
	def set_blancas(self, cantidad):
		pass
	def limpiar_tablero(self):
		pass
	def get_tablero(self):
		pass
	def llenar_tablero(self,row,i):
		pass   
	def llenar_fichas(self,row):
		pass