from abc import ABC, abstractmethod

class InterfazAbs(ABC):
	def __init__(self):
		pass 
		
	# Para mostrar un mensaje
	def message_display(self,text):
		pass
	
	# Para cerrar la interfaz
	def quit(self):
		pass
	
	# Metodo que mostrara las reglas segun lo quiera el diseñador
	def ver_reglas(self):
		pass
		
	def mostrar_tablero(self):
		pass
		
	# Resetar la interfaz para que se muetre una nueva partida
	def partida_nueva(self):
		pass

	def text_objects(self,text, font,color):
		pass

	def font_render(self, name,option):
		pass

	def click_box(self, pos,option):
		pass

	def button(self,msg,x,y,w,h,color1,color2,color3, action=None):
		pass

		
		