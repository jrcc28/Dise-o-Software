from Interfaz import *
from Jugador import Jugador
from Pieza import Pieza
from Validador import Validador
from Tablero import Tablero
import csv
import pygame
from ControladorAbs import ControladorAbs
#to windows compile: py -m pip install -U pygame --user
#windows use: >py -m Controlador

class Controlador(ControladorAbs):
	def __init__(self):
		self.interfaz = Interfaz(self)
		self.validador = Validador()
		self.tablero = Tablero(8,8) # Crea un tablero 8 x 8  
		self.turno = 1

		#se instancian los jugadores
		self.jugador1 = Jugador(Pieza(1,1),"Jugador 1") # Jugador con piezas negras
		self.jugador2 = Jugador(Pieza(2,2),"Jugador 2") # Jugador con piezas blancas
		self.nombreIngresado2 = ""
		self.nombreIngresado1 = ""
		#posiciones del tablero y tamanos
		self.espacioVentanaTablero = 50
		self.cuadro = 50
		self.borde = 20
		self.tableroPos = 30
		self.BOARD_SIZE = 400


	def start(self):
		self.interfaz.game_menu()

	def get_tablero(self):
		return self.tablero.get_tablero()

	def get_turno(self):
		return self.turno

    #por el momento solo csv
	def leer_archivo(self, name):
		count_info=0
		count_lineas=1
		with open(name , newline='') as File:
			reader = csv.reader(File)
			for row in reader:
				if count_lineas % 2!=0:
					if count_info < 8 :
						self.tablero.llenar_tablero(row,count_info)
					else:
						self.turno=self.tablero.llenar_fichas(row)

					count_info=count_info+1

				count_lineas=count_lineas+1

    #por el momento solo csv
	def crear_archivo(self, name):
		myFile = open(name, 'w')
		with myFile:
			writer = csv.writer(myFile)
			writer.writerows(self.tablero.get_valores_tablero())
			writer.writerows(self.validador.get_estado_juego(self.turno, self.tablero))

	def reset(self):
		self.tablero.limpiar_tablero()
		self.validador.reset_validador()
		self.turno=1
		#se vuelven a crear los jugadores
		self.jugador1 = Jugador(Pieza(1,1),"Jugador 1")
		self.jugador2 = Jugador(Pieza(2,2),"Jugador 2")
		
	def jugar_turno(self,x,y):
		pos_valida = self.convertir_pos(x,y)
		#esto es para colocar alguna ficha en el tablero(matriz) debe ser una posicion valida
		if self.turno==1 and pos_valida!=(-1,-1):#si el jugador es ficha negra
			if self.validador.set_ficha(pos_valida[0], pos_valida[1], 1, self.tablero):#si se logro colocar la ficha
				self.set_turno(2) # ahora pasa a ser la ficha blanca
				self.validador.cambiar_turno(2, self.tablero)
				if not self.validador.hay_movimientos_validos(self.tablero):
					self.set_turno(1)
					self.validador.cambiar_turno(1, self.tablero)
		elif self.turno==2 and pos_valida!=(-1,-1):#si el jugador es ficha blanca
			if self.validador.set_ficha(pos_valida[0], pos_valida[1], 2, self.tablero):#si se logro colocar la ficha
				self.set_turno(1)
				self.validador.cambiar_turno(1, self.tablero)
				if not self.validador.hay_movimientos_validos(self.tablero):
					self.set_turno(2)
					self.validador.cambiar_turno(2, self.tablero)


	def setNombreJugador1(self):
		self.jugador1.set_nombre(self.nombreIngresado1)
		

	def getNombreJugador1(self):
		self.jugador1.set_nombre(self.nombreIngresado1)
		return self.jugador1.get_nombre()

	def setNombreJugador2(self):
		self.jugador2.set_nombre(self.nombreIngresado2)

	def getNombreJugador2(self):
		self.jugador2.set_nombre(self.nombreIngresado2)
		return self.jugador2.get_nombre()

	def get_reglas(self):
		#string con las reglas.
		reglas = ["El objetivo del juego es tener mas fichas del propio color.",
		"De inicio se colocan cuatro fichas como en el tablero:",
		"Dos fichas blancas en D4 y E5, y dos negras en E4 y D5.",
		"Comienzan a mover las negras: Un movimiento consiste",
		"en colocar una ficha propia sobre el tablero de",
		"forma que \'flanquee\' una o varias fichas contrarias.",
		"Las fichas flanqueadas son volteadas para mostrar",
		"el color propio. Es obligatorio voltear todas",
		"las fichas flanqueadas entre la ficha que se coloca",
		"y las que ya estaban colocadas.",
		"Una vez volteadas las fichas el turno pasa al contrario",
		"que procede de la misma forma con sus fichas.",
		"Si un jugador no tiene ninguna posibilidad",
		"de mover, el turno pasa al contrario.",
		"La partida termina cuando ninguno de los dos jugadores puede mover.",
		"Normalmente cuando el tablero esta lleno o practicamente lleno.",
		"Gana el jugador que acaba con mas fichas propias",
		"sobre el tablero Es posible el empate.",
		"Disfruta el Juego!"]
		return reglas

	def set_turno(self, valor):
		self.turno = valor

		
	#busca la cantidad de piezas en el tablero de una pieza especifica
	def get_num_piezas(self, pieza):
		return self.tablero.get_num_piezas(pieza)
		
	def get_mover_negras(self):
		return self.validador.get_mover_negras()

	def get_mover_blancas(self):
		return self.validador.get_mover_blancas()
		
	def get_filas(self):
		return self.tablero.get_filas()
		
	def get_columnas(self):
		return self.tablero.get_columnas()

	def convertir_pos(self,mouse_x ,mouse_y ):
		# click was out of board, ignores
		if mouse_x > self.BOARD_SIZE + self.espacioVentanaTablero or \
			mouse_x < self.espacioVentanaTablero or \
			mouse_y > self.BOARD_SIZE + self.espacioVentanaTablero or \
			mouse_y < self.espacioVentanaTablero:
			position = (-1,-1)
			return position

		# find place
		position = ((mouse_x - self.espacioVentanaTablero) // self.cuadro),((mouse_y - self.espacioVentanaTablero) // self.cuadro)
		# flip orientation
		position = (position[1], position[0])
		continar = False
		return position

	def eventos_reglas(self):
		for tipoEvento in pygame.event.get():
			if tipoEvento.type == pygame.QUIT:
					self.interfaz.quit()

			if tipoEvento.type == pygame.KEYDOWN:
				if tipoEvento.key == pygame.K_ESCAPE:
					self.interfaz.blit()
					return False
		return True
		
	def eventos_menu(self):
		for tipoEvento in pygame.event.get():
			if tipoEvento.type == pygame.QUIT:
					self.interfaz.quit()
		return True

	
	def eventos_tablero(self):
		for tipoEvento in pygame.event.get():
			if tipoEvento.type == pygame.QUIT:
				self.interfaz.quit()
			
			elif tipoEvento.type == pygame.KEYDOWN:
				if tipoEvento.key == pygame.K_ESCAPE:
					self.interfaz.blit()
					return False
			
			elif tipoEvento.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				self.jugar_turno(pos[0],pos[1])
		

		return True

	def eventos_elegir_color(self,active1,active2):
		
		for tipoEvento in pygame.event.get():
			if tipoEvento.type == pygame.QUIT:
					self.interfaz.quit()
				
			if tipoEvento.type == pygame.KEYDOWN:
				if tipoEvento.key == pygame.K_ESCAPE:
					self.interfaz.blit()
					return False
						
				if tipoEvento.key== pygame.K_RETURN:
					self.interfaz.guardar_jugadores()
					
						
				if active1:
					if tipoEvento.key == pygame.K_BACKSPACE:
						self.nombreIngresado1 = self.nombreIngresado1[:-1]		
					else:
						self.nombreIngresado1 += tipoEvento.unicode
					# Re-render the text.
					
					self.interfaz.font_render(self.nombreIngresado1,1)

				if active2:
					if tipoEvento.key == pygame.K_BACKSPACE:
						self.nombreIngresado2 = self.nombreIngresado2[:-1]
					else:
						self.nombreIngresado2 += tipoEvento.unicode
						
						# Re-render the text.

					self.interfaz.font_render(self.nombreIngresado2,2)

				
			if tipoEvento.type ==  pygame.MOUSEBUTTONDOWN:
				# If the user clicked on the input_box rect.
				if self.interfaz.click_box(tipoEvento.pos,1):
				# Toggle the active variable.
					return 2
				# If the user clicked on the input_box rect.
				if self.interfaz.click_box(tipoEvento.pos,2):
					# Toggle the active variable.
					return 3


		return True
		
		


def main():
	controlador = Controlador()
	controlador.start()


if __name__ == '__main__':
	main()
