from TableroAbs import TableroAbs
from Pieza import Pieza

class Tablero(TableroAbs):
	def __init__(self):
		self.board = [[Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0)],
			[Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0)],
			[Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(3,3), Pieza(0,0), Pieza(0,0), Pieza(0,0)],
			[Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(1,1), Pieza(2,2), Pieza(3,3), Pieza(0,0), Pieza(0,0)],
			[Pieza(0,0), Pieza(0,0), Pieza(3,3), Pieza(2,2), Pieza(1,1), Pieza(0,0), Pieza(0,0), Pieza(0,0)],
			[Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(3,3), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0)],
			[Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0)],
			[Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0)]]
			#self.mover_negra=True
			#self.mover_blanca=True
		self.num_negras=2
		self.num_blancas=2

	def get_num_negras(self):
		return self.num_negras

	def get_num_blancas(self):
		return self.num_blancas

	def set_negras(self, cantidad):
		self.num_negras = cantidad

	def set_blancas(self, cantidad):
		self.num_blancas = cantidad

	def limpiar_tablero(self):
		self.board = [[Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0)],
			[Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0)],
			[Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(3,3), Pieza(0,0), Pieza(0,0), Pieza(0,0)],
			[Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(1,1), Pieza(2,2), Pieza(3,3), Pieza(0,0), Pieza(0,0)],
			[Pieza(0,0), Pieza(0,0), Pieza(3,3), Pieza(2,2), Pieza(1,1), Pieza(0,0), Pieza(0,0), Pieza(0,0)],
			[Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(3,3), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0)],
			[Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0)],
			[Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0), Pieza(0,0)]]
		#self.mover_negra=True
		#self.mover_blanca=True
		self.num_negras=2
		self.num_blancas=2

	def get_tablero(self):
		return self.board

	def llenar_tablero(self,row,i):
		for j in range(8):
			print("%s,%s",i,j)
			self.board[i][j].set_color(row[j])

	def llenar_fichas(self,row):
		self.num_negras=int(row[0])
		self.num_blancas=int(row[1])

		if int(row[3])==1:
			self.mover_negra=True
		else:
			self.mover_negra=False

		if int(row[4])==1:
			self.mover_blanca=True
		else:
			self.mover_blanca=0

		return int(row[2])
