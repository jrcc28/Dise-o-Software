#!/usr/bin/python
# -*- coding: latin-1 -*-
import time
import pygame
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

        #posiciones del tablero y tamanos
        self.cuadro = 50
        self.borde = 20
        self.tableroPos = 30
        self.BOARD_SIZE = 400

        #primerJugador, 1 es negra por reglas empieza primero, 2 es blancas
        self.primero = 1
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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        reglas = False
                        self.win.blit(self.fondo,(0,0))

            self.win.blit(self.fondo,(0,0))
			
			#solicita las reglas al juego y las coloca en pantalla
			###Nota: intentar mejorar esto para no llamar tantas veces al metodo
            for x in range(len(self.controlador.get_reglas())):
                self.message_display(self.controlador.get_reglas()[x],450,20+(30*x),self.white,20)
				
            self.button("Para Volver presione BACKSPACE",290,630,300,50,self.red, self.red, self.black, self.salir)
            pygame.display.update()
            self.win.blit(self.fondo,(0,0))



    def mostrar_tablero(self):
        jugar=True
        seguir=True
        while jugar:
            if not self.controlador.get_mover_negras() or not self.controlador.get_mover_blancas():
                seguir=False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        jugar = False
                        self.win.blit(self.fondo,(0,0))
                elif event.type == pygame.MOUSEBUTTONUP and seguir:
                    pos = pygame.mouse.get_pos()         
                    self.controlador.jugar_turno(pos[0],pos[1])


            #se muestra el fondo
            self.win.blit(self.fondo,(0,0))
            #se muestran botones
            self.button("Ver Reglas",490,30,150,100,self.bright_blue, self.blue, self.black, self.ver_reglas)
            self.button("Para Volver presione BACKSPACE",490,290,300,100,self.red, self.red, self.black, self.salir)
            self.button("Guardar Partida",490,160,150,100,self.bright_green, self.green, self.black, self.guardar_partida)

            if seguir:
                if self.controlador.get_turno() == 1:
                    self.message_display("Turno de las negras.",590,420,self.white,20)
                elif self.controlador.get_turno() == 2:
                    self.message_display("Turno de las blancas.",590,420,self.white,20)
            else:
                if self.controlador.get_num_negras()> self.controlador.get_num_blancas():
                    self.message_display("Ganaron las Negras!!!!!",590,420,self.white,20)

                if self.controlador.get_num_negras()< self.controlador.get_num_blancas():
        	        self.message_display("Ganaron las Blancas!!!!!",590,420,self.white,20)

                if self.controlador.get_num_negras()== self.controlador.get_num_blancas():
        	        self.message_display("Empate!!!!!",590,420,self.white,20)


				
            #se muestra el tablero
            self.win.blit(self.board,(30,30))

            #colocar fichas sobre tablero(imagen
            #print(self.controlador.get_tablero())
            tablero = self.controlador.get_tablero()
            #print(tablero)
            for fila in range(8):
                for colunm in range(8):
                    if tablero[fila][colunm] == 1:
                        
                        self.win.blit(self.blackToken,((self.cuadro*colunm)+self.tableroPos+self.borde,(self.cuadro*fila)+self.tableroPos+self.borde))
                    elif tablero[fila][colunm] == 2:
                        
                        self.win.blit(self.whiteToken,((self.cuadro*colunm)+self.tableroPos+self.borde,(self.cuadro*fila)+self.tableroPos+self.borde))
                    elif tablero[fila][colunm] == 3:
                        
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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        escoger = False
                        self.win.blit(self.fondo,(0,0))

            self.win.blit(self.fondo,(0,0))
            self.button("Para Volver presione BACKSPACE",280,500,300,100, self.red, self.red, self.black, self.salir)
            self.button("Cargar Partida",340,300,170,100, self.bright_black, self.grey ,self.white, self.cargar_partida)
            self.button("Nueva Partida", 340,100,170,100, self.bright_white, self.white ,self.black, self.partida_nueva)
            pygame.display.update()




    def elegir_color(self):
        escoger=True
        while escoger:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        escoger = False
                        self.win.blit(self.fondo,(0,0))

            self.win.blit(self.fondo,(0,0))
            self.button("Para Volver presione BACKSPACE",280,500,300,100, self.red, self.red, self.black, self.salir)
            self.button("Negras",340,300,170,100, self.bright_black, self.grey ,self.white, self.elegir_negras)
            self.button("Blancas", 340,100,170,100, self.bright_white, self.white ,self.black, self.elegir_blancas)
            pygame.display.update()

    def elegir_blancas(self):
        self.primero = 2
        self.win.blit(self.fondo,(0,0))
        self.message_display("                                           El jugador ha escogido las fichas blancas.",(300),(500/2),self.white,30)
        pygame.display.update()
        time.sleep(1)

    def elegir_negras(self):
    	self.primero = 1
    	self.win.blit(self.fondo,(0,0))
    	self.message_display("                                           El jugador ha escogido las fichas negras.",(300),(500/2),self.white,30)
    	pygame.display.update()
    	time.sleep(1)

    #metodo del boton donde
    #msg es el texto del boton
    #x y w h son las cordenadas del boton x,y, height y width
    #color1 es el color del boton cuando se selecciona
    #color2 es el color cuando no se toca
    #color3 es el color del texto
    #action es el objeto del metodo que ejecuta el boton
    def button(self,msg,x,y,w,h,color1,color2,color3, action):
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
        intro=True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   intro = False

            self.win.blit(self.fondo,(0,0))

            self.message_display("OTHELLO",(900/2),(500/2),self.white,100)

            #botones de las opciones
            self.button("Ver Reglas",640,400,170,100, self.bright_blue, self.blue, self.black, self.ver_reglas)
            self.button("Elegir Color",40,400,170,100, self.bright_green, self.green,self.black, self.elegir_color)
            self.button("Jugar", 340,400,170,100, self.bright_red, self.red, self.black, self.opciones_juego)
            pygame.display.update()
            self.clock.tick(15)

        pygame.quit()
