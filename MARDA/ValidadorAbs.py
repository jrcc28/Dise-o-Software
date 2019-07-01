from abc import ABC, abstractmethod

class ValidadorAbs(ABC):
	def __init__(self):
		pass 
		
	# Verifica si hay jugadas posibles a realizar
	def hay_movimientos_validos(self, tablero):
		pass
		
	# Retorna los movimientos permitidos en un turno, dado a como se encuentre el tablero en ese momento
	def get_movimientos_permitidos(self, pieza, tablero):
		pass
		
	# Pone la ficha en el tablero, solo cuando es una jugada valida
	def set_ficha(self, fila, columna, valor, tablero):
		pass
	
	# Resetea el validador a sus valores por defecto
	def reset_validador(self):
		pass
		
	def cambiar_turno(self, valor, tablero):
		pass
	