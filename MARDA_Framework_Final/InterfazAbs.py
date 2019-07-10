from abc import ABC, abstractmethod
import time
import pygame
from PiezaAbs import *
from ControladorAbs import *


class InterfazAbs(ABC):
	"""
	Clase Interfaz Abstracta.
	"""

	def __init__(self, controlador, i , width, height, fondo, board):
		"""
		Constructor de la clase Interfaz.
		"""
		self.controlador = controlador


		pygame.init()
		#sprites
		#se llenan con el fondo y tablero que el usuario desee con la direccion de la imagen
		self.fondo = pygame.image.load(fondo)
		self.board = pygame.image.load(board)

		#colores

		#window
		self.win = pygame.display.set_mode((width, height))

		#primerJugador = i tipo de pieza del primero
		self.primero = i



	def message_display(self,text,x,y,color, fontsize):
		"""
		Este metodo funciona para mostrar texto en pantalla.
		Parametros:
		text = linea de texto a ser mostrada
		x, y = coordenadas dentro de la ventana
		color = color del texto
		fontsize = size de la letra
		"""
		largeText = pygame.font.Font('freesansbold.ttf',fontsize)
		TextSurf, TextRect = self.text_objects(text, largeText,color)
		TextRect.center = (x,y)
		self.win.blit(TextSurf, TextRect)



	def text_objects(self,text,font,color):
		"""
		Este metodo funciona para poner texto en pantalla.
		Parametros:
		text = texto a colocar.
		font = tipo de letra.
		color = color de letra.
		"""
		textSurface = font.render(text, True, color)
		return textSurface, textSurface.get_rect()


	def quit(self):
		"""
		Metodo que se utiliza para salir del programa o ventana.
		Retorna un evento tipo pygame.quit(), de esta forma se desactiva
		la libreria pygame.
		"""
		pygame.quit()

	#actualizar ventana con el fondo que el usuario desea
	"""
	Metodo que actualiza la ventana con el fondo que el usuario desee.
	El fondo debe estar declarado como atributo de la clase interfaz.
	"""
	def blit(self):
		self.win.blit(self.fondo,(0,0))


	def ver_reglas(self):
		"""
		Metodo para mostrar las reglas del juego en pantalla.
		"""
		reglas=True
		while reglas:

			reglas = self.controlador.eventos_reglas()
			reglas_juego = self.controlador.get_reglas()

			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON




	def mostrar_tablero(self, width, height):
		"""
		Metodo para mostrar el tablero en pantalla.
		Parametros:
		width: Ancho del tablero.
		height: Altura del tablero.
		"""
		jugar=True
		while jugar:

			jugar=self.controlador.eventos_tablero()

			#se muestra el tablero con un width y height que el usuario desee cambiandolo
			self.win.blit(self.board,(width,height))
			tablero = self.controlador.get_tablero()

			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON



	#para una partida nueva no requiere cambios

	def partida_nueva(self):
		"""
		Metodo que reinicia el tablero, para poder iniciar una nueva partida.
		"""
		self.controlador.reset()
		self.mostrar_tablero()


	def opciones_juego(self):
		"""
		Metodo para mostrar reglas del juego.
		"""
		escoger=True
		while escoger:
			escoger = self.controlador.eventos_reglas()

			self.win.blit(self.fondo,(0,0))
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON


	def elegir_color(self):
		"""
		Metodo para mostrar opciones para escoger color del jugador.
		"""


		escoger=True
		while escoger:

			escoger = self.controlador.eventos_elegir_color()

			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON




	def guardar_jugadores(self):
		"""
		Metodo para guardar los nombres de los jugadores que se ingresen por pantalla.
		"""
		#AQUI SE GUARDAN LOS NOMBRES DE LOS JUFADORES MEDIANTE EL CONTROLADOR
		self.win.blit(self.fondo,(0,0))
		self.controlador.setNombreJugador2()
		self.controlador.setNombreJugador1()
		#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
		#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
		#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
		#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
		#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
		#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON



	def button(self,msg,x,y,w,h,color1,color2,color3, action=None):
		"""
		Metodo para crear y mostrar un boton.
		Parametros:
		msg = es el texto del boton
		x,y,w,h = son las cordenadas del boton x,y, height y width
		color1 = es el color del boton cuando se selecciona
		color2 = es el color cuando no se toca
		color3 = es el color del texto
		action = es el objeto del metodo que ejecuta el boton
		"""
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		#si el mouse esta encima del boton cambia de color
		if x+w > mouse[0] > x and y+h > mouse[1] > y:
			pygame.draw.rect(self.win, color1,(x,y,w,h))

			#click se ejecuta el metodo
			if click[0] == 1 and action != None:
				action()
		else:
			pygame.draw.rect(self.win, color2,(x,y,w,h))

		#texto del boton
		self.message_display(msg,(x+(w/2)),(y+(h/2)),color3,17)
		#clock.tick(15)


	#menu del juego

	def game_menu(self):
		"""
		Metodo que muestra la pantalla o menu inicial del juego.
		"""
		## ESTA INTERFAZ APLICA PARA TODOS
		intro=True
		while intro:
			intro = self.controlador.eventos_menu()
			self.win.blit(self.fondo,(0,0))

			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON
			#AQUI VAN POSIBLES BOTONES O TEXTO QUE EL USUARIO DESEE PONER MEDIANTE LOS METOOD DE MESSAGE DISPLAY Y BUTTON

		pygame.quit()
