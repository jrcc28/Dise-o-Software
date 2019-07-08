from abc import ABC, abstractmethod

cfrom Pieza import Pieza

class Tablero(ABC):
#recibe la cantidad de filas y columnas y llena el tablero de fichas vacias
	def __init__(self, filas,columnas):
		self.board = []
		self.filas=filas
		self.columnas=columnas
		self.fichas_totales=0
		self.fichas_invalidas=0
		self.fichas_vacias=0
		self.fichas_validas=0
		
		self.board = [0] * filas
		for i in range(filas):
			self.board[i] = [] * columnas
		
		for i in range(filas):
			for j in range(columnas):
				self.board[i].append(Pieza(self.fichas_vacias,self.fichas_vacias))
		
				
		
#busca la cantidad de piezas en el tablero de una pieza especifica
	def get_num_piezas(self, pieza):
		num_piezas=0
		for i in range(self.filas):
			for j in range(self.columnas):
				if self.board[i][j].get_color() == pieza:
					num_piezas+=1
		
		return num_piezas
		
	
#restea el tablero a estado inicial
	def limpiar_tablero(self):
		for i in range(self.filas):
			for j in range(self.columnas):
				self.board[i][j]=Pieza(self.fichas_vacias,self.fichas_vacias)
				
				
	def get_filas(self):
		return self.filas
		
	def get_columnas(self):
		return self.columnas
		

	def get_tablero(self):		
		return self.board

		
	def get_fichas_totales(self):
		return self.fichas_totales
		
	def get_fichas_invalidas(self):
		return self.fichas_invalidas
		
	def get_fichas_vacias(self):
		return self.fichas_vacias
		
		
	def get_fichas_validas(self):
		return self.fichas_validas
