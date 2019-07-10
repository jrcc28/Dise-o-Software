from abc import ABC, abstractmethod
from TableroAbs import *
from PiezaAbs import *


class ValidadorAbs(ABC):
	"""
	Clase Validador abstracto.
	"""

	def __init__(self):
		"""
		Constructor de la clase Validador.
		"""
		#se agregan total de piezas con i siendo el tipo de pieza
		# si son 6 piezas se agregan 6 de estas variables para cada pieza
		self.mover_pieza_i=True

	def reset_validador(self):
		"""
		Este metodo resetea los valores del validador, para que vuelva a iniciar.
		"""
		##se agregan total de piezas con i siendo el tipo de pieza
		#de igual manera para todas las piezas del juego
		self.mover_pieza_i=True

	# Verifica si hay jugadas posibles a realizar

	def hay_movimientos_validos(self, tablero):
		"""
		Metodo que verifica si existen posiciones validas o posibles para jugar en el tablero.
		Parametros:
		Tablero = tablero donde se realiza la comprobacion de posicion valida.
		Retorna:
		Verdadero si existen posiciones validas.
		False si no existen posiciones validas.
		"""
		#con un valor en el tablero que sea valido, se busca dicho valor en el tablero
		mi_tablero = tablero.get_tablero()
		for i in range(tablero.get_filas()):
			for j in range(tablero.get_columnas()):
				if mi_tablero[i][j].get_color() == tablero.get_fichas_validas():
					return True
		return False

	# Retorna los movimientos permitidos en un turno, dado a como se encuentre el tablero en ese momento

	def get_movimientos_permitidos(self, pieza, tablero):
		"""
		Este metodo busca movimientos permitidos segun el turno actual,
		un tipo de pieza
		y el estado actual del tablero.
		Parametros:
		Pieza = tipo de pieza a la cual se verifica los movimientos permitidos.
		Tablero = tablero donde se realiza la comprobacion.
		Retorna:
		Un vector de pares con las posiciones permitidas. En caso de que no existan
		retorna un vector vacio.
		"""
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

	# Pone la ficha en el tablero, solo cuando es una jugada valida

	def set_ficha(self, fila, columna, valor, tablero):
		"""
		Este metodo coloca una ficha en el tablero, solo cuando es una jugada o
		posicion valida.
		Parametros:
		Fila = numero de fila donde se intenta poner la pieza.
		Columna = numero de columna donde se intenta poner la pieza.
		Valor = valor que se va a colocar en la posicion.
		Tablero = tablero donde se va a realizar la validacion.
		Retorna:
		Verdadero si se coloco la ficha.
		Falso si no se coloco la ficha.
		"""
		#solo se permite en posiciones validas
		mi_tablero = tablero.get_tablero()
		if mi_tablero[fila][columna].get_color() == tablero.get_fichas_validas():
			mi_tablero[fila][columna].set_color(valor)


		if not self.hay_movimientos_validos(tablero):
			return True

		return False


	def cambiar_turno(self, valor, tablero):
		"""
		Metodo para cambiar el turno de jugador.
		Parametros:
		Valor = valor a cambiar.
		Tablero = tablero donde se realiza la validacion de cambio de turno.
		Retorna:
		Verdadero si no cambio turno.
		Falso si cambio turno.
		"""
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


	def buscar_pos_validas(self,i,j, fila, columna, color, tablero):
		"""
		Metodo que busca posiciones validas dentro del tablero segun un color o valor.
		Parametros:
		i = fila del tablero.
		j = columna del tablero.
		color = color a verificar las posiciones validas.
		tablero = tablero donde se realiza la validacion.
		"""
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
