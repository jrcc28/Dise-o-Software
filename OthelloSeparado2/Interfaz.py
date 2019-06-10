#!/usr/bin/python
# -*- coding: latin-1 -*-
import time
import pygame
from Pieza import Pieza
from Controlador import Controlador

class Interfaz:
	def __init__(self, controlador):
		self.controlador = controlador

		pygame.init()
		#sprites
		self.fondo = pygame.image.load('images/fondo.jpg')
		self.board = pygame.image.load('images/board.bmp')
		self.whiteToken = pygame.image.load('images/blanca.bmp')
		self.blackToken = pygame.image.load('images/negra.bmp')
		self.availableToken = pygame.image.load('images/posible.jpg')

		#window
		self.win = pygame.display.set_mode((900, 700))
		pygame.display.set_caption("OTHELLO")

		#colores
		self.white = (255,255,255)
		self.black = (0,0,0)
		self.red = (200,0,0)
		self.green = (0,200,0)
		self.blue = (0, 0, 200)
		self.bright_red = (255,0,0)
		self.bright_green = (0,255,0)
		self.bright_blue = (0, 0, 255)
		self.bright_white = (200, 200, 200)
		self.bright_black = (70,70,70)
		self.grey = (128,128,128)

		#colores para botones
		self.button_ver_reglas_press = (190, 190, 12)
		self.button_ver_reglas = (243, 243, 68)

		self.button_back = (234, 158, 35)

		self.button_play = (40, 193, 244)
		self.button_play_press = (12, 143, 187)

		self.button_color = (32, 178, 170)
		self.button_color_press = (0, 139, 139)

		self.button_cargar = (121,207,46)
		self.button_cargar_press = (95,172,27)

		self.button_guardar = (76,238,224)
		self.button_guardar_press = (24,177,163)

		#posiciones del tablero y tamanos
		self.cuadro = 50
		self.borde = 20
		self.tableroPos = 30
		self.BOARD_SIZE = 400

		#primerJugador, 1 es negra por reglas empieza primero, 2 es blancas
		self.primero = 1
		self.nombreIngresado1 =''
		self.nombreIngresado2 =''
		self.clock = pygame.time.Clock()

	#para mostrar texto
	def message_display(self,text,x,y,color, fontsize):
		largeText = pygame.font.Font('freesansbold.ttf',fontsize)
		TextSurf, TextRect = self.text_objects(text, largeText,color)
		TextRect.center = (x,y)
		self.win.blit(TextSurf, TextRect)

	#para procesar texto
	def text_objects(self,text, font,color):
		textSurface = font.render(text, True, color)
		return textSurface, textSurface.get_rect()

	def salir(self):
		return False

	def ver_reglas(self):
		reglas=True
		while reglas:
			Eventos = self.controlador.get_eventos()
			for tipoEvento in Eventos:
				if tipoEvento.type == pygame.QUIT:
					pygame.quit()

				if tipoEvento.type == pygame.KEYDOWN:
					if tipoEvento.key == pygame.K_ESCAPE:
						reglas = False
						self.win.blit(self.fondo,(0,0))

			self.win.blit(self.fondo,(0,0))

			#solicita las reglas al juego y las coloca en pantalla
			###Nota: intentar mejorar esto para no llamar tantas veces al metodo
			for x in range(len(self.controlador.get_reglas())):
				self.message_display(self.controlador.get_reglas()[x],450,50+(30*x),self.white,20)

			self.button("Para Volver presione ESC",290,630,300,50,self.button_back, self.button_back, self.black, self.salir)
			pygame.display.update()
			self.win.blit(self.fondo,(0,0))

	def mostrar_tablero(self):
		jugar=True
		seguir=True
		while jugar:
			Eventos = self.controlador.get_eventos()
			for tipoEvento in Eventos:
				if tipoEvento.type == pygame.QUIT:
					pygame.quit()
				elif tipoEvento.type == pygame.KEYDOWN:
					if tipoEvento.key == pygame.K_ESCAPE:
						jugar = False
						self.win.blit(self.fondo,(0,0))
				elif tipoEvento.type == pygame.MOUSEBUTTONUP:
					pos = pygame.mouse.get_pos()
					self.controlador.jugar_turno(pos[0],pos[1])


			if not self.controlador.get_mover_negras() and not self.controlador.get_mover_blancas():
				seguir=False
			#se muestra el fondo
			textj1= "Fichas Negras de "
			textj2= "Fichas Blancas de "
			self.win.blit(self.fondo,(0,0))
			#se muestran botones
			self.button("Ver Reglas",490,30,150,100,self.button_ver_reglas_press, self.button_ver_reglas, self.black, self.ver_reglas)
			self.button("Guardar Partida",490,160,150,100,self.button_guardar_press, self.button_guardar, self.black, self.guardar_partida)
			self.button("Para Volver presione ESC",490,290,300,100,self.button_back, self.button_back, self.black, self.salir)
			textj1 += self.controlador.getNombreJugador1()
			textj2 += self.controlador.getNombreJugador2()
			self.message_display(textj1 + ":  " +str(self.controlador.get_num_negras()),590,500,self.white,20)
			self.message_display(textj2 + ":  "+str(self.controlador.get_num_blancas()),590,550,self.white,20)
			text = "Turno de "
			ganador = "Gano "
			if seguir:
				if self.controlador.get_turno() == 1:
					text += self.controlador.getNombreJugador1()
					self.message_display(text,590,450,self.white,20)
				elif self.controlador.get_turno() == 2:
					text += self.controlador.getNombreJugador2()
					self.message_display(text,590,450,self.white,20)
			else:
				if self.controlador.get_num_negras()> self.controlador.get_num_blancas():
					ganador += self.controlador.getNombreJugador1()
					ganador += "!!"
					self.message_display(ganador,590,450,self.white,20)

				if self.controlador.get_num_negras()< self.controlador.get_num_blancas():
					ganador += self.controlador.getNombreJugador2()
					ganador += "!!"
					self.message_display(ganador,590,450,self.white,20)

				if self.controlador.get_num_negras()== self.controlador.get_num_blancas():
					self.message_display("Empate!!!!!",590,450,self.white,20)



			#se muestra el tablero
			self.win.blit(self.board,(30,30))

			#colocar fichas sobre tablero(imagen
			#print(self.controlador.get_tablero())
			tablero = self.controlador.get_tablero()
			#print(tablero)
			for fila in range(8):
				for colunm in range(8):
					if tablero[fila][colunm].get_color() == 1:
						self.win.blit(self.blackToken,((self.cuadro*colunm)+self.tableroPos+self.borde,(self.cuadro*fila)+self.tableroPos+self.borde))
					elif tablero[fila][colunm].get_color() == 2:
						self.win.blit(self.whiteToken,((self.cuadro*colunm)+self.tableroPos+self.borde,(self.cuadro*fila)+self.tableroPos+self.borde))
					elif tablero[fila][colunm].get_color() == 3:
						self.win.blit(self.availableToken,((self.cuadro*colunm)+self.tableroPos+self.borde,(self.cuadro*fila)+self.tableroPos+self.borde))

			pygame.display.update()

	def cargar_partida(self):
		self.controlador.leer_archivo("prueba.csv")
		self.mostrar_tablero()

	def partida_nueva(self):
		self.controlador.reset()
		self.mostrar_tablero()

	def guardar_partida(self):
		self.controlador.crear_archivo("prueba.csv")

	def opciones_juego(self):
		escoger=True
		while escoger:
			Eventos = self.controlador.get_eventos()
			for tipoEvento in Eventos:
				if tipoEvento.type == pygame.QUIT:
					pygame.quit()

				if  tipoEvento.type == pygame.KEYDOWN:
					if tipoEvento.key == pygame.K_ESCAPE:
						escoger = False
						self.win.blit(self.fondo,(0,0))

			self.win.blit(self.fondo,(0,0))
			self.button("Para Volver presione ESC",280,500,300,100, self.button_back, self.button_back, self.black, self.salir)
			self.button("Cargar Partida",340,300,170,100, self.button_cargar_press, self.button_cargar ,self.black, self.cargar_partida)
			self.button("Nueva Partida", 340,100,170,100, self.bright_white, self.white ,self.black, self.partida_nueva)
			pygame.display.update()

	def elegir_color(self):
		rect1 = pygame.Rect(530, 85, 200, 32)
		active1 = False
		rect2 = pygame.Rect(530, 185, 200, 32)
		active2 = False
		FONT = pygame.font.Font(None, 32)
		txt_surface1 = FONT.render(self.nombreIngresado1, True, self.white)
		txt_surface2 = FONT.render(self.nombreIngresado2, True, self.white)
		escoger=True
		while escoger:
			Eventos = self.controlador.get_eventos()
			for tipoEvento in Eventos:			
				if tipoEvento.type == pygame.QUIT:
					pygame.quit()
				if tipoEvento.type == pygame.KEYDOWN:
					if tipoEvento.key == pygame.K_ESCAPE:
						escoger = False
						self.win.blit(self.fondo,(0,0))
					if tipoEvento== pygame.K_RETURN:
						self.guardar_jugadores()
						print(self.nombreIngresado1)
						print(self.nombreIngresado2)
					if active1:
						if tipoEvento.key == pygame.K_BACKSPACE:
							self.nombreIngresado1 = self.nombreIngresado1[:-1]
						else:
							self.nombreIngresado1 += tipoEvento.unicode
						# Re-render the text.
						txt_surface1 = FONT.render(self.nombreIngresado1, True, self.white)
					if active2:
						if tipoEvento.key == pygame.K_BACKSPACE:
							self.nombreIngresado2 = self.nombreIngresado2[:-1]
						else:
							self.nombreIngresado2 += tipoEvento.unicode
							# Re-render the text.
						txt_surface2 = FONT.render(self.nombreIngresado2, True, self.white)
				if tipoEvento.type ==  pygame.MOUSEBUTTONDOWN:
					# If the user clicked on the input_box rect.
					if rect1.collidepoint(tipoEvento.pos):
					# Toggle the active variable.
						active1 = not active1
					else:
						active1 = False
					# If the user clicked on the input_box rect.
					if rect2.collidepoint(tipoEvento.pos):
					# Toggle the active variable.
						active2 = not active2
					else:
						active2 = False

			self.win.blit(self.fondo,(0,0))
			self.win.blit(txt_surface1,(535,90))
			self.win.blit(txt_surface2,(535,190))
			self.name_button("",530, 85, 200, 32, self.button_guardar_press, self.button_guardar, self.black)
			self.name_button("",530, 185, 200, 32, self.button_guardar_press, self.button_guardar, self.black)
			#pygame.draw.rect(self.win, self.white,rect1,2)
			#pygame.draw.rect(self.win, self.white,rect2,2)
			self.button("Para volver presione ESC",300,400,250,50, self.button_back, self.button_back, self.black, self.salir)
			self.button("Guardar nombres",325,330,200,50, self.button_guardar_press, self.button_guardar, self.black, self.guardar_jugadores)
			self.message_display("Nombre del jugador 1 (Fichas Negras):",330,100,self.white, 20)
			self.message_display("Nombre del jugador 2 (Fichas Blancas):",330,200,self.white, 20)
			pygame.display.update()

	def guardar_jugadores(self):
		self.win.blit(self.fondo,(0,0))
		self.message_display("                                      Guardando nombres de jugadores.",(300),(500/2),self.white,30)
		pygame.display.update()
		time.sleep(1)
		#aca se guardan los nombres
		self.controlador.setNombreJugador1(self.nombreIngresado1)
		self.controlador.setNombreJugador2(self.nombreIngresado2)
		self.win.blit(self.fondo,(0,0))
		self.message_display("                                      Nombres guardados.",(300),(500/2),self.white,30)
		pygame.display.update()
		time.sleep(1)

	#metodo del boton donde
	#msg es el texto del boton
	#x y w h son las cordenadas del boton x,y, height y width
	#color1 es el color del boton cuando se selecciona
	#color2 es el color cuando no se toca
	#color3 es el color del texto
	#action es el objeto del metodo que ejecuta el boton
	def button(self,msg,x,y,w,h,color1,color2,color3, action=None):
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

	def name_button(self,msg,x,y,w,h,color1,color2,color3, action=None):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		#si el mouse esta encima del boton cambia de color
		if x+w > mouse[0] > x and y+h > mouse[1] > y:
			pygame.draw.rect(self.win, color1,(x,y,w,h),2)

			#click se ejecuta el metodo
			if click[0] == 1 and action != None:
				action()
		else:
			pygame.draw.rect(self.win, color2,(x,y,w,h),2)

		#texto del boton
		#self.message_display(msg,(x+(w/2)),(y+(h/2)),color3,17)
		#clock.tick(15)

	#menu del juego
	def game_menu(self):
		intro=True
		while intro:
			Eventos = self.controlador.get_eventos()
			for tipoEvento in Eventos:
				if tipoEvento.type == pygame.QUIT:
				   intro = False

			self.win.blit(self.fondo,(0,0))

			self.message_display("OTHELLO",(900/2),(500/2),self.white,100)

			#botones de las opciones
			self.button("Ver Reglas",640,400,170,100, self.button_ver_reglas_press, self.button_ver_reglas, self.black, self.ver_reglas)
			self.button("Elegir Color",40,400,170,100, self.button_color_press, self.button_color,self.black, self.elegir_color)
			self.button("Jugar", 340,400,170,100, self.button_play_press, self.button_play, self.black, self.opciones_juego)
			pygame.display.update()
			self.clock.tick(15)

		pygame.quit()
