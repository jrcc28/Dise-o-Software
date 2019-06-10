from Tablero import *
from Pieza import Pieza

class Validador:
	def __init__(self):
		self.mover_negra=True
		self.mover_blanca=True

	def get_mover_negras(self):
		return self.mover_negra

	def reset_validador(self):
		self.mover_negra = True
		self.mover_blanca = True

	def get_mover_blancas(self):
		return self.mover_blanca

	def hay_movimientos_validos(self, tablero):
		mi_tablero = tablero.get_tablero()
		for i in range(8):
			for j in range(8):
				if mi_tablero[i][j].get_color() == 3:
					return True
		return False

	def cambiar_turno(self, valor, tablero):
		num_blancas = tablero.get_num_blancas()
		num_negras = tablero.get_num_negras()
		if self.get_movimientos_permitidos(valor, tablero)==[] or num_blancas + num_negras==64:
			if valor==1:
				self.mover_negra=False
			else:
				self.mover_blanca=False

			return False

		return True

	def get_movimientos_permitidos(self, color, tablero):
		mi_tablero = tablero.get_tablero()
		if color== 1:
			color_otro = 2
		else:
			color_otro = 1

		pos_validas = []

		for i in range(8):
			for j in range(8):
				if mi_tablero[i][j].get_color() == color:
					pos_validas = pos_validas + self.escanear_pos(i, j, color, mi_tablero)
				if mi_tablero[i][j].get_color()==3:
					mi_tablero[i][j].set_color(0)


		pos_validas = list(set(pos_validas))


		print(pos_validas)
		for x in pos_validas:
			i=int(x[0])
			j=int(x[1])
			tablero.board[i][j].set_color(3)

		return pos_validas

	def buscar_pos_validas(self,i,j, fila, columna, color_otro, mi_tablero):
		mov_fila= i-fila
		mov_col= j-columna

		pos_validas=[]

		if (i < 8 and i >= 0  and  j < 8 and j >= 0 and mi_tablero[i][j].get_color() == color_otro):
			i = i + mov_fila
			j = j + mov_col
			while (i < 8 and i >= 0  and  j < 8 and j >= 0  and mi_tablero[i][j].get_color() == color_otro):
				i = i + mov_fila
				j = j + mov_col
			if (i < 8 and i >= 0  and  j < 8 and j >= 0 and mi_tablero[i][j].get_color() == 0):
				pos_validas = pos_validas + [(i, j)]


		return pos_validas


	def escanear_pos(self, fila, columna, color, mi_tablero):
		if (fila < 0 or fila > 7 or columna < 0 or columna > 7):
			return pos_validas

		if color == 1:
			color_otro = 2
		else:
			color_otro = 1

		pos_validas = []


		i = fila - 1
		j = columna
		pos_validas= pos_validas + self.buscar_pos_validas(i, j , fila , columna , color_otro, mi_tablero)


		i = fila - 1
		j = columna + 1
		pos_validas= pos_validas + self.buscar_pos_validas(i, j , fila , columna , color_otro, mi_tablero)

		i = fila
		j = columna + 1
		pos_validas= pos_validas + self.buscar_pos_validas(i, j , fila , columna , color_otro, mi_tablero)

		i = fila + 1
		j = columna + 1
		pos_validas= pos_validas + self.buscar_pos_validas(i, j , fila , columna , color_otro, mi_tablero)

		i = fila + 1
		j = columna
		pos_validas= pos_validas + self.buscar_pos_validas(i, j , fila , columna , color_otro, mi_tablero)


		i = fila + 1
		j = columna - 1
		pos_validas= pos_validas + self.buscar_pos_validas(i, j , fila , columna , color_otro, mi_tablero)


		i = fila
		j = columna - 1
		pos_validas= pos_validas + self.buscar_pos_validas(i, j , fila , columna , color_otro, mi_tablero)



		i = fila - 1
		j = columna - 1
		pos_validas= pos_validas + self.buscar_pos_validas(i, j , fila , columna , color_otro, mi_tablero)

		return pos_validas


	def get_estado_juego(self, turno, tablero): # VALIDADOR
		estado = [[0,0,0,0,0]]
		estado[0][0] = tablero.get_num_negras()
		estado[0][1] = tablero.get_num_blancas()
		estado[0][2] = turno
		if self.mover_negra:
			estado[0][3]=1
		else:
			estado[0][3]=0

		if self.mover_blanca:
			estado[0][4]=1
		else:
			estado[0][4]=0

		return estado


	def set_ficha(self, fila, columna, valor, tablero):
		#solo se permite en posiciones validas
		mi_tablero = tablero.get_tablero()
		if mi_tablero[fila][columna].get_color() == 3:
			mi_tablero[fila][columna].set_color(valor)

			for i in range(1, 9):
				self.flip(i,fila,columna,valor, tablero)

			if valor==1:
				tablero.set_negras(tablero.get_num_negras() + 1)


			elif valor==2:
				tablero.set_blancas(tablero.get_num_blancas() + 1)

			return True


		if not self.hay_movimientos_validos(tablero):
			return True

		return False




	def aplicar_flip(self, color_otro, fila_flip, colum_flip, i, j, tablero, color):
		pos_validas = []
		if i in range(8) and j in range(8) and tablero.board[i][j].get_color() == color_otro:

			pos_validas = pos_validas + [(i, j)]
			i = i + fila_flip
			j = j + colum_flip
			while i in range(8) and j in range(8) and tablero.board[i][j].get_color() == color_otro:

				pos_validas = pos_validas + [(i, j)]
				i = i + fila_flip
				j = j + colum_flip
			if i in range(8) and j in range(8) and tablero.board[i][j].get_color() == color:

				for pos in pos_validas:

					tablero.board[pos[0]][pos[1]].set_color(color)
					if color == 1:
						tablero.set_negras(tablero.get_num_negras() + 1)
						tablero.set_blancas(tablero.get_num_blancas() - 1)
					else:
						tablero.set_blancas(tablero.get_num_blancas() + 1)
						tablero.set_negras(tablero.get_num_negras() - 1)





	def flip(self, direction, fila,columna, color, tablero):

		fila_flip = -1
		colum_flip = 0
		if direction == 2:

			fila_flip = -1
			colum_flip = 1

		elif direction == 3:

			fila_flip = 0
			colum_flip = 1

		elif direction == 4:

			fila_flip = 1
			colum_flip = 1

		elif direction == 5:

			fila_flip = 1
			colum_flip = 0

		elif direction == 6:

			fila_flip = 1
			colum_flip = -1

		elif direction == 7:

			fila_flip = 0
			colum_flip = -1

		elif direction == 8:

			fila_flip = -1
			colum_flip = -1

		i = fila + fila_flip
		j = columna + colum_flip

		if color == 1:
			color_otro = 2
		else:
			color_otro = 1

		self.aplicar_flip(color_otro, fila_flip, colum_flip, i, j, tablero, color)
