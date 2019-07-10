from abc import ABC, abstractmethod

from PiezaAbs import *

class Tablero(ABC):
	"""
	Clase Tablero abstracto.
	"""
#recibe la cantidad de filas y columnas y llena el tablero de fichas vacias
	def __init__(self, filas,columnas):
		"""
		Constructor de la clase tablero.
		Parametros:
		Filas = cantidad de filas que va a contener el tablero.
		Columnas = cantidad de columnas que va a contener el tablero.
		"""
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
		"""
		Metodo que retorna la cantidad de un tipo de piezas existentes sobre el tablero.
		Parametros:
		pieza = tipo de pieza a ser buscada sobre el tablero.
		"""
		num_piezas=0
		for i in range(self.filas):
			for j in range(self.columnas):
				if self.board[i][j].get_color() == pieza:
					num_piezas+=1

		return num_piezas


#restea el tablero a estado inicial

	def limpiar_tablero(self):
		"""
		Metodo que reinicia el tablero a un estado inicial.
		"""
		for i in range(self.filas):
			for j in range(self.columnas):
				self.board[i][j]=Pieza(self.fichas_vacias,self.fichas_vacias)


	def get_filas(self):
		"""
		Metodo que retorna la cantidad de filas del tablero.
		"""
		return self.filas

	def get_columnas(self):
		"""
		Metodo que retorna la cantidad de columnas del tablero.
		"""
		return self.columnas


	def get_tablero(self):
		"""
		Metodo que retorna el tablero de la clase.
		"""
		return self.board


	def get_fichas_totales(self):
		"""
		Metodo que retorna la cantidad de fichas totales sobre el tablero.
		"""
		return self.fichas_totales


	def get_fichas_invalidas(self):
		"""
		Metodo que retorna la cantidad de fichas invalidadas sobre el tablero.
		"""
		return self.fichas_invalidas


	def get_fichas_vacias(self):
		"""
		Metodo que retorna la cantidad de fichas vacias sobre el tablero.
		"""
		return self.fichas_vacias


	def get_fichas_validas(self):
		"""
		Metodo que retorna la cantidad de fichas validas sobre el tablero.
		"""
		return self.fichas_validas
