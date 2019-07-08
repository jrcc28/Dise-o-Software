#!/usr/bin/python
# -*- coding: latin-1 -*-
import time
import pygame
from Pieza import Pieza
from Controlador import Controlador
from InterfazAbs import InterfazAbs

class Interfaz(InterfazAbs):
	def __init__(self, controlador):
		self.controlador = controlador

	
		pygame.init()
		#sprites

		#colores

		#window
		self.win = pygame.display.set_mode((900, 700))
		
		
		#posiciones del tablero y tamanos
		self.cuadro = 50
		self.borde = 20
		self.tableroPos = 30
		self.BOARD_SIZE = 400

		#primerJugador = i tipo de pieza del primero
		self.primero = i
		
		

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

	def quit(self):
		pygame.quit()

	def blit(self):
		self.win.blit(self.fondo,(0,0))



	def ver_reglas(self):
		reglas=True
		while reglas:
			
			reglas = self.controlador.eventos_reglas()

			self.win.blit(self.fondo,(0,0))

			for x in range(len(self.controlador.get_reglas())):
				self.message_display(self.controlador.get_reglas()[x],450,50+(30*x),self.white,20)

			self.button("Para Volver presione ESC",290,630,300,50,self.button_back, self.button_back, self.black, self.salir)
			pygame.display.update()
			self.win.blit(self.fondo,(0,0))

	
	def mostrar_tablero(self):
		jugar=True
		seguir=True
		while jugar:
			jugar=self.controlador.eventos_tablero()
			
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
			self.message_display(textj1 + ":  " +str(self.controlador.get_num_piezas(1)),590,500,self.white,20)
			self.message_display(textj2 + ":  "+str(self.controlador.get_num_piezas(2)),590,550,self.white,20)
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
				if self.controlador.get_num_piezas(1)> self.controlador.get_num_piezas(2):
					ganador += self.controlador.getNombreJugador1()
					ganador += "!!"
					self.message_display(ganador,590,450,self.white,20)

				if self.controlador.get_num_piezas(1)< self.controlador.get_num_piezas(2):
					ganador += self.controlador.getNombreJugador2()
					ganador += "!!"
					self.message_display(ganador,590,450,self.white,20)

				if self.controlador.get_num_piezas(1)== self.controlador.get_num_piezas(2):
					self.message_display("Empate!!!!!",590,450,self.white,20)


			#se muestra el tablero
			self.win.blit(self.board,(30,30))
			#print("Tablero mostrado")

			#colocar fichas sobre tablero(imagen
			#print(self.controlador.get_tablero())
			tablero = self.controlador.get_tablero()
			#print(tablero)
			for fila in range(self.controlador.get_filas()):
				for colunm in range(self.controlador.get_columnas()):
					if tablero[fila][colunm].get_color() == 1:
						self.win.blit(self.blackToken,((self.cuadro*colunm)+self.tableroPos+self.borde,(self.cuadro*fila)+self.tableroPos+self.borde))
					elif tablero[fila][colunm].get_color() == 2:
						self.win.blit(self.whiteToken,((self.cuadro*colunm)+self.tableroPos+self.borde,(self.cuadro*fila)+self.tableroPos+self.borde))
					elif tablero[fila][colunm].get_color() == 3:
						self.win.blit(self.availableToken,((self.cuadro*colunm)+self.tableroPos+self.borde,(self.cuadro*fila)+self.tableroPos+self.borde))

			pygame.display.update()

	

	def partida_nueva(self):
		self.controlador.reset()
		self.mostrar_tablero()

	
	def opciones_juego(self):
		escoger=True
		while escoger:
			escoger = self.controlador.eventos_reglas()
			
			self.win.blit(self.fondo,(0,0))
			self.button("Para Volver presione ESC",280,500,300,100, self.button_back, self.button_back, self.black, self.salir)
			self.button("Cargar Partida",340,300,170,100, self.button_cargar_press, self.button_cargar ,self.black, self.cargar_partida)
			self.button("Nueva Partida", 340,100,170,100, self.bright_white, self.white ,self.black, self.partida_nueva)
			pygame.display.update()

	def font_render(self, name,option):
		if option ==1:
			self.txt_surface1= self.FONT.render(name, True, self.white)	

		elif option==2:
			self.txt_surface2=self.FONT.render(name, True, self.white)

	def click_box(self, pos,option):	

		if option ==1:
		
			return self.rect1.collidepoint(pos)
		

		elif option==2:
			
			return self.rect2.collidepoint(pos)

	def elegir_color(self):
		
		self.FONT = pygame.font.Font(None, 32)
		
		self.font_render('',1)
		self.font_render('',2)
		escoger=True
		active1 = False
		active2 = False
		while escoger:
			if escoger==2:
			
				active1 = True
				active2 = False
			
			elif escoger==3:
				active1 = False
				active2=True

			
			
			
			escoger = self.controlador.eventos_elegir_color(active1,active2)		

			self.win.blit(self.fondo,(0,0))
			self.win.blit(self.txt_surface1,(535,90))
			self.win.blit(self.txt_surface2,(535,190))
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
		self.controlador.setNombreJugador2()
		self.controlador.setNombreJugador1()
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

	
	#menu del juego
	def game_menu(self):
		## ESTA INTERFAZ APLICA PARA TODOS
		#AQUI SOLO SE CAMBIA LA PARTE NOMBRE DEL JUEGO POR EL QUE DESEE EL USUARIO
		intro=True
		while intro:
			intro = self.controlador.eventos_menu()
			self.win.blit(self.fondo,(0,0))

			self.message_display("NOMBRE DEL JUEGO",(900/2),(500/2),self.white,100)

			#botones de las opciones
			self.button("Ver Reglas",640,400,170,100, self.button_ver_reglas_press, self.button_ver_reglas, self.black, self.ver_reglas)
			self.button("Elegir Color",40,400,170,100, self.button_color_press, self.button_color,self.black, self.elegir_color)
			self.button("Jugar", 340,400,170,100, self.button_play_press, self.button_play, self.black, self.opciones_juego)
			pygame.display.update()
			self.clock.tick(15)

		pygame.quit()
