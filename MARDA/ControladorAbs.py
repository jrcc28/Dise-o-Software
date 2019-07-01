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