from abc import ABC, abstractmethod

class TableroAbs(ABC):
	def __init__(self):
		pass 
	def limpiar_tablero(self):
		pass
	def get_tablero(self):
		pass
	def llenar_tablero(self,row,i):
		pass   
	def llenar_fichas(self,row):
		pass