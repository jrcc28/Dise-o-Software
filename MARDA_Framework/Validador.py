from ValidadorAbs import ValidadorAbs
from Tablero import *
from Pieza import Pieza

class Validador(ValidadorAbs):
	def __init__(self):
		#se agregan total de piezas con i siendo el tipo de pieza
		# si son 6 piezas se agregan 6 de estas variables para cada pieza
		self.mover_pieza_i=True
		

	
	def reset_validador(self):
		##se agregan total de piezas con i siendo el tipo de pieza
		#de igual manera para todas las piezas del juego
		self.mover_pieza_i=True

	

	def hay_movimientos_validos(self, tablero):
		#con un valor en el tablero que sea valido, se busca dicho valor en el tablero
		mi_tablero = tablero.get_tablero()
		for i in range(tablero.get_filas()):
			for j in range(tablero.get_columnas()):
				if mi_tablero[i][j].get_color() == tablero.get_fichas_validas():
					return True
		return False

	def cambiar_turno(self, valor, tablero):
		#se agregan total de piezas con i siendo el tipo de pieza
		num_pieza_i = tablero.get_num_piezas(i)
		num_pieza_i = tablero.get_num_piezas(i)
		#ve si puede mover la siguienre ficha viendo si quedan posibles movimientos o ya esta lleno el tablero
		#de igual manera se agrega num_pieza_i para cada valor
		if self.get_movimientos_permitidos(valor, tablero)==[] or num_pieza_i + num_pieza_i ==tablero.get_fichas_totales():
			if valor==i:
				self.mover_pieza_i=False

			return False

		return True

	def get_movimientos_permitidos(self, color, tablero):
		mi_tablero = tablero.get_tablero()
		pos_validas = []

		#con este metodo se buscan los posibles movimientos de una ficha i mediante su color
		for i in range(tablero.get_filas()):
			for j in range(tablero.get_columnas()):
				if mi_tablero[i][j].get_color() == color:
					pos_validas = pos_validas + self.escanear_pos(i, j, color, tablero)
				if mi_tablero[i][j].get_color()==tablero.get_fichas_validas():
					mi_tablero[i][j].set_color(tablero.get_fichas_vacias())


		pos_validas = list(set(pos_validas))
		for x in pos_validas:
			i=int(x[0])
			j=int(x[1])
			tablero.board[i][j].set_color(tablero.get_fichas_validas())

		return pos_validas

	def buscar_pos_validas(self,i,j, fila, columna, color, tablero):
		#este metodo se encarga de buscar posciones validads medinte el algortimo del juego especifico
		mov_fila= i-fila
		mov_col= j-columna
		mi_tablero = tablero.get_tablero()
		pos_validas=[]
		
		#algoritmo de pos validas aqui
		#algoritmo de pos validas aqui
		#algoritmo de pos validas aqui
		#algoritmo de pos validas aqui

		return pos_validas


	def escanear_pos(self, fila, columna, color, mi_tablero):
		#verifica si es valida incialmente con los limites del tablero
		if (fila < 0 or fila > tablero.get_filas() or columna < 0 or columna > tablero.get_columnas()):
			return pos_validas

		pos_validas = []

		#esto se realiza para todos los vecinos de la posicion donde se encuentra la ficha buscando posiciones validas segun la posicion dada
		#aqui unos ejemplos con tres vecinos pero se debe adaptar segun el tablero la mayoria cuadrado seran con 8 posibles vecinos
		i = fila - 1
		j = columna
		pos_validas= pos_validas + self.buscar_pos_validas(i, j , fila , columna , color, mi_tablero)

		#asi se obtendran todas las posibles posiciones de donde se puede colocar la ficha 


		return pos_validas
	


	def set_ficha(self, fila, columna, valor, tablero):
		#solo se permite en posiciones validas
		mi_tablero = tablero.get_tablero()
		if mi_tablero[fila][columna].get_color() == tablero.get_fichas_validas():
			mi_tablero[fila][columna].set_color(valor)


		if not self.hay_movimientos_validos(tablero):
			return True

		return False

