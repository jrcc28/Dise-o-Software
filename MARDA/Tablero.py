from TableroAbs import TableroAbs
from Pieza import Pieza

class Tablero(TableroAbs):
#recibe la cantidad de filas y columnas y llena el tablero de fichas vacias
	def __init__(self, filas,columnas):
		self.board = []
		self.filas=filas
		self.columnas=columnas
		self.fichas_totales=64
		self.fichas_invalidas=-1
		self.fichas_vacias=0
		self.fichas_validas=3
		
		
		self.board = [0] * filas
		for i in range(filas):
			self.board[i] = [] * columnas
		
		for i in range(filas):
			for j in range(columnas):
				self.board[i].append(Pieza(self.fichas_vacias,self.fichas_vacias))
		

		# NEGRAS = TIPO 1
		# BLANCAS = TIPO 2
		self.board[3][3] = Pieza(1, 1)
		self.board[3][4] = Pieza(2, 2)
		self.board[4][3] = Pieza(2, 2)
		self.board[4][4] = Pieza(1, 1)
		
				
		
#busca la cantidad de piezas en el tablero de una pieza especifica
	def get_num_piezas(self, pieza):
		num_piezas=0
		for i in range((self.filas - 1)):
			for j in range((self.columnas - 1)):
				if self.board[i][j].get_tipo()== pieza:
					num_piezas=num_piezas+1
		
		return num_piezas
		
	

	
#restea el tablero a estado inicial
	def limpiar_tablero(self):
		for i in range(self.filas):
			self.board.append([])
			for j in range(self.columnas):
				self.board.append(Pieza(self.fichas_vacias,self.fichas_vacias))
				
				
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
		
#retorna el tablero pero no en piezas si no en valores int que definen el tipo de pieza	
	def get_valores_tablero(self):
		tablero_valores=[]
		
		for i in range(self.filas):
			tablero_valores.append([])
			for j in range(self.columnas):
				tablero_valores.append(self.board[i][j].get_tipo())
		
		
			
		return tablero_valores

#llena el tablero cuando se hacer cargar
	def llenar_tablero(self,row,i):
		for i in range(self.filas):
			self.board[i][j].set_color(row[j])
			self.board[i][j].set_tipo(row[j])
