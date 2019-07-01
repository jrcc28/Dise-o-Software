#from Controlador import Controlador
from Tablero import *
from Validador import *
class Juego:
	def __init__(self):
		self.tablero = Tablero(8, 8)
		self.validador = Validador()

	def get_num_negras(self):
		return self.tablero.get_num_negras()

	def get_num_blancas(self):
		return self.tablero.get_num_blancas()

	def get_mover_negras(self):
		return self.validador.get_mover_negras()

	def get_mover_blancas(self):
		return self.validador.get_mover_blancas()
		
	def get_num_piezas(self, pieza):
		return self.tablero.get_num_piezas(pieza)
		
		
	def get_filas(self):
		return self.tablero.get_filas)
		
	def get_columnas(self):
		return self.tablero.get_columnas()

	def clean_game(self):
		self.tablero.limpiar_tablero()
		self.validador.reset_validador()

	def get_tablero(self):
		return self.tablero.get_tablero()
		
	def get_valores_tablero(self):		
		return self.tablero.get_valores_tablero()

	def hay_movimientos_validos(self):
		return self.validador.hay_movimientos_validos(self.tablero)

	def get_estado_juego(self,turno):
		return self.validador.get_estado_juego(turno, self.tablero)

	def llenar_tablero(self,row,i):
		self.tablero.llenar_tablero(row, i)

	def llenar_fichas(self,row):
		return self.tablero.llenar_fichas(row)

	def flip(self, direction, fila, columna, color):
		self.validador.flip(direction, fila, columna, color, self.tablero)

	def set_ficha(self, fila, columna, valor):
		return self.validador.set_ficha(fila, columna, valor, self.tablero)

	def cambiar_turno(self,valor):
		return self.validador.cambiar_turno(valor, self.tablero)

	def escanear_pos(self, fila, columna, color):
		return self.validador.escanear_pos(fila, columna, color, self.tablero)

	def get_movimientos_permitidos(self, color):
		return self.validador.get_movimientos_permitidos(color, self.tablero)
