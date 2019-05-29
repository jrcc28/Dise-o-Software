from Tablero import *
class Validador:
	def __init__(self):
		self.mover_negra=True
		self.mover_blanca=True

	def get_mover_negras(self):
		return self.mover_negra

	def get_mover_blancas(self):
		return self.mover_blanca

	def hay_movimientos_validos(self, tablero): 
		mi_tablero = tablero.get_tablero()
		for i in range(8):
			for j in range(8):
				if mi_tablero[i][j] == 3:
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
		if color == 1:
			other = 2
		else:
			other = 1

		places = []

		for i in range(8):
			for j in range(8):
				if mi_tablero[i][j] == color:
					places = places + self.escanear_pos(i, j, color, mi_tablero)
				if mi_tablero[i][j]==3:
					mi_tablero[i][j]=0
					

		places = list(set(places))
		
				
		#print(places)
		for x in places:
			i=int(x[0])
			j=int(x[1])
			tablero.board[i][j]=3

		return places
		
		
	def escanear_pos(self, fila, columna, color, mi_tablero):
		
		if color == 1:
			other = 2
		else:
			other = 1

		places = []

		if (fila < 0 or fila > 7 or columna < 0 or columna > 7):
			return places



		# north
		i = fila - 1
		if (i >= 0 and mi_tablero[i][columna] == other):
			i = i - 1
			while (i >= 0 and mi_tablero[i][columna] == other):
				i = i - 1
			if (i >= 0 and mi_tablero[i][columna] == 0):
				places = places + [(i, columna)]

		# northeast
		i = fila - 1
		j = columna + 1
		if (i >= 0 and j < 8 and mi_tablero[i][j] == other):
			i = i - 1
			j = j + 1
			while (i >= 0 and j < 8 and mi_tablero[i][j] == other):
				i = i - 1
				j = j + 1
			if (i >= 0 and j < 8 and mi_tablero[i][j] == 0):
				places = places + [(i, j)]

		# east
		j = columna + 1
		if (j < 8 and mi_tablero[fila][j] == other):
			j = j + 1
			while (j < 8 and mi_tablero[fila][j] == other):
				j = j + 1
			if (j < 8 and mi_tablero[fila][j] == 0):
				places = places + [(fila, j)]

		# southeast
		i = fila + 1
		j = columna + 1
		if (i < 8 and j < 8 and mi_tablero[i][j] == other):
			i = i + 1
			j = j + 1
			while (i < 8 and j < 8 and mi_tablero[i][j] == other):
				i = i + 1
				j = j + 1
			if (i < 8 and j < 8 and mi_tablero[i][j] == 0):
				places = places + [(i, j)]

		# south
		i = fila + 1
		if (i < 8 and mi_tablero[i][columna] == other):
			i = i + 1
			while (i < 8 and mi_tablero[i][columna] == other):
				i = i + 1
			if (i < 8 and mi_tablero[i][columna] == 0):
				places = places + [(i, columna)]

		# southwest
		i = fila + 1
		j = columna - 1
		if (i < 8 and j >= 0 and mi_tablero[i][j] == other):
			i = i + 1
			j = j - 1
			while (i < 8 and j >= 0 and mi_tablero[i][j] == other):
				i = i + 1
				j = j - 1
			if (i < 8 and j >= 0 and mi_tablero[i][j] == 0):
				places = places + [(i, j)]

		# west
		j = columna - 1
		if (j >= 0 and mi_tablero[fila][j] == other):
			j = j - 1
			while (j >= 0 and mi_tablero[fila][j] == other):
				j = j - 1
			if (j >= 0 and mi_tablero[fila][j] == 0):
				places = places + [(fila, j)]

		# northwest
		i = fila - 1
		j = columna - 1
		if (i >= 0 and j >= 0 and mi_tablero[i][j] == other):
			i = i - 1
			j = j - 1
			while (i >= 0 and j >= 0 and mi_tablero[i][j] == other):
				i = i - 1
				j = j - 1
			if (i >= 0 and j >= 0 and mi_tablero[i][j] == 0):
				places = places + [(i, j)]

		return places
		
		
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
		if mi_tablero[fila][columna] == 3:
			mi_tablero[fila][columna] = valor
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
		
		
	def flip(self, direction, fila,columna, color, tablero): # AQUI SI HAY QUE USAR EL TABLERO DE LA CLASE TABLERO, NO UNA COPIA
		if direction == 1:
			# north
			row_inc = -1
			col_inc = 0
		elif direction == 2:
			# northeast
			row_inc = -1
			col_inc = 1
		elif direction == 3:
			# east
			row_inc = 0
			col_inc = 1
		elif direction == 4:
			# southeast
			row_inc = 1
			col_inc = 1
		elif direction == 5:
			# south
			row_inc = 1
			col_inc = 0
		elif direction == 6:
			# southwest
			row_inc = 1
			col_inc = -1
		elif direction == 7:
			# west
			row_inc = 0
			col_inc = -1
		elif direction == 8:
			# northwest
			row_inc = -1
			col_inc = -1

		places = []     # pieces to flip
		i = fila + row_inc
		j = columna + col_inc

		if color == 1:
			other = 2
		else:
			other = 1

		if i in range(8) and j in range(8) and tablero.board[i][j] == other:
			# assures there is at least one piece to flip
			print(1)
			places = places + [(i, j)]
			i = i + row_inc
			j = j + col_inc
			while i in range(8) and j in range(8) and tablero.board[i][j] == other: # AQUI SI HAY QUE USAR EL TABLERO EN SI, NO UNA COPIA
				# search for more pieces to flip
				places = places + [(i, j)]
				i = i + row_inc
				j = j + col_inc
			if i in range(8) and j in range(8) and tablero.board[i][j] == color:
				# found a piece of the right color to flip the pieces between
				for pos in places:
					# flips
					tablero.board[pos[0]][pos[1]] = color
					if color == 1:
						tablero.set_negras(tablero.get_num_negras() + 1) 
						tablero.set_blancas(tablero.get_num_blancas() - 1)
					else:
						tablero.set_blancas(tablero.get_num_blancas() + 1)
						tablero.set_negras(tablero.get_num_negras() - 1) 