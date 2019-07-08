from abc import ABC, abstractmethod

class ControladorAbs(ABC):
	def __init__(self):
		pass 
		
	# Comienza el juego
	def start(self):
		pass
		
	def get_tablero(self):
		pass
		
	# Resetea el juego, se vuelven a los valores por defecto
	def reset(self):
		pass
		
	def set_turno(self, valor):
		pass

	def get_turno(self):
		pass
	
	def get_reglas(self):
		pass
		
	def get_turno(self):
		pass
		
	#busca la cantidad de piezas en el tablero de una pieza especifica
	def get_num_piezas(self, pieza):
		pass
		
	def get_filas(self):
		pass
		
	def get_columnas(self):
		pass
		
	def setNombreJugador1(self,nombre):
		pass

	def getNombreJugador1(self):
		pass

	def setNombreJugador2(self,nombre):
		pass

	def getNombreJugador2(self):
		pass
		
	def convertir_pos(self,mouse_x ,mouse_y ):
		pass