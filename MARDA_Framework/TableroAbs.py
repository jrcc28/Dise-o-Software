from abc import ABC, abstractmethod

class TableroAbs(ABC):
	def __init__(self):
		pass 
		
	#restea el tablero a estado inicial
	def limpiar_tablero(self):
		pass
	
	def get_tablero(self):
		pass
	
	#llena el tablero cuando se hacer cargar
	def llenar_tablero(self,row,i):
		pass  

		
	#retorna el tablero pero no en piezas si no en valores int que definen el tipo de pieza	
	def get_valores_tablero(self):
		pass
	
	#busca la cantidad de piezas en el tablero de una pieza especifica
	def get_num_piezas(self, pieza):
		pass
		
		
	def get_filas(self):
		pass
		
	def get_columnas(self):
		pass
	
	def get_fichas_totales(self):
		pass
		
	def get_fichas_invalidas(self):
		pass
		
	def get_fichas_vacias(self):
		pass
		
		
	def get_fichas_validas(self):
		pass