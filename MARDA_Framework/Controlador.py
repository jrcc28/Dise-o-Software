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
		#con estas variables se crea un tablero con filas=f y columnas=c
		#ademas la variable turno sera para el que es el jugador que juega en cada intante siendo i el tipo de pieza o colo a como se quiera definir
		self.tablero = Tablero(f,c) # Crea un tablero 8 x 8  
		self.turno = i

		#se instancian los jugadores
		#todos los juegos tienen dos jugadores 
		#donde i = tipo de pieza y j = color de pieza
		self.jugador1 = Jugador(Pieza(i,j),"Jugador 1") # Jugador con piezas negras
		self.jugador2 = Jugador(Pieza(i,j),"Jugador 2") # Jugador con piezas blancas
		self.nombreIngresado2 = ""
		self.nombreIngresado1 = ""
		#posiciones del tablero y tamanos
		#dichas variables para el tablero y distintos aspectos de dicho que se pueden cambiar a como desee el usuario del framework
		self.espacioVentanaTablero = 
		self.cuadro = 
		self.borde = 
		self.tableroPos = 
		self.BOARD_SIZE = 


	def start(self):
		#inicia la interfaz
		self.interfaz.game_menu()

	def get_tablero(self):
		return self.tablero.get_tablero()

	def get_turno(self):
		return self.turno

	def reset(self):
		##este metodo resetea el estado del juego 
		self.tablero.limpiar_tablero()
		self.validador.reset_validador()
		#con el turno i = tipo de ficha que se juega primerp
		self.turno=i
		#se vuelven a crear los jugadores
		#donde i = tipo de pieza y j = color de pieza
		self.jugador1 = Jugador(Pieza(i,j),"Jugador 1")
		self.jugador2 = Jugador(Pieza(i,j),"Jugador 2")
		
	def jugar_turno(self,x,y):
		pos_valida = self.convertir_pos(x,y)
		#esto es para colocar alguna ficha en el tablero(matriz) debe ser una posicion valida
		##este metodo realza la accion de jugar un turno cambiando el turno a la ficha que sigue
		#donde i= es el tipo de ficha con el turno actual y j = el tipo de ficha que sigue
		if self.turno==i and pos_valida!=(-1,-1):#pos valida en el rango del tablero con el mouse
			if self.validador.set_ficha(pos_valida[0], pos_valida[1], i, self.tablero):#si se logro colocar la ficha
				self.set_turno(j) # ahora pasa a la siguiente tipo de ficha
				self.validador.cambiar_turno(j, self.tablero)
				if not self.validador.hay_movimientos_validos(self.tablero):
					self.set_turno(i)
					self.validador.cambiar_turno(i, self.tablero)
		


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
		#se llena el vector con las reglas del juego
		reglas = ["AQUI VAN LAS REGLAS"]
		return reglas

	def set_turno(self, ficha_que_sigue):
		#setea al la pieza que sigue
		self.turno = ficha_que_sigue

		
	#busca la cantidad de piezas en el tablero de una pieza especifica
	def get_num_piezas(self, pieza):
		return self.tablero.get_num_piezas(pieza)
		
	def get_filas(self):
		return self.tablero.get_filas()
		
	def get_columnas(self):
		return self.tablero.get_columnas()

	def convertir_pos(self,mouse_x ,mouse_y ):
		#CON ESTE METODO SE CONVIERTE LA POSICION DEL MOUESE EN UNA POSICION DEL TABLERO VALIDA SEGUN LOS PARAMETROS ESTABLECIDOS 
		#POR EL USUARIO DEL FRAMEWORK
		if mouse_x > self.BOARD_SIZE + self.espacioVentanaTablero or \
			mouse_x < self.espacioVentanaTablero or \
			mouse_y > self.BOARD_SIZE + self.espacioVentanaTablero or \
			mouse_y < self.espacioVentanaTablero:
			position = (-1,-1)
			return position

		
		position = ((mouse_x - self.espacioVentanaTablero) // self.cuadro),((mouse_y - self.espacioVentanaTablero) // self.cuadro)
		position = (position[1], position[0])
		continar = False
		return position

	
	#METODOS DE EVENTOS QUE APLICAN PARA TODOS LOS JUEGOS DE TABLER0

	#TODOS DEBEN TENER UNA OPCION PARA MOSTRAR REGLAS
	def eventos_reglas(self):
		for tipoEvento in pygame.event.get():
			if tipoEvento.type == pygame.QUIT:
					self.interfaz.quit()

			if tipoEvento.type == pygame.KEYDOWN:
				if tipoEvento.key == pygame.K_ESCAPE:
					self.interfaz.blit()
					return False
		return True
		
	#TODOS DEBEN TENER UNA OPCION DEL GAME MENU INICIAL
	def eventos_menu(self):
		for tipoEvento in pygame.event.get():
			if tipoEvento.type == pygame.QUIT:
					self.interfaz.quit()
		return True

	
	#TODOS DEN TENER UNA OPCION QUE MUESTRE TABLERO
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



	#TODOS TIENEN DOS JUGADORES Y UNA OPCION DONDE SE ELIGA COLOR O TIPO DE FICHAS 
	#Y SE ASIGNEN NOMBRES DE JUGADOR
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


		return True
		
		


def main():
	controlador = Controlador()
	controlador.start()


if __name__ == '__main__':
	main()
