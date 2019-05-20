#!/usr/bin/python
# -*- coding: latin-1 -*-
import time
import pygame

class Interfaz:
    def __init__(self):
        pygame.init()
        #sprites
        self.fondo = pygame.image.load('images/fondo.jpg')
        self.board = pygame.image.load('images/board.bmp')
        self.whiteToken = pygame.image.load('images/blanca.bmp')
        self.blackToken = pygame.image.load('images/negra.bmp')

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
        #posiciones del tablero
        self.cuadro = 50
        self.borde = 20
        self.tableroPos = 30
        #primerJugador, 1 es negra por reglas empieza primero, 2 es blancaas
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
            self.message_display("El objetivo del juego es tener mas fichas del propio color.",450,10,self.white,20)
            self.message_display("De inicio se colocan cuatro fichas como en el diagrama.",450,40,self.white,20)
            self.message_display("Dos fichas blancas en D4 y E5, y dos negras en E4 y D.",450,70,self.white,20)
            self.message_display("Comienzan a mover las negras. Un movimiento consiste",450,100,self.white,20)
            self.message_display("en colocar una ficha propia sobre el tablero de",450,130,self.white,20)
            self.message_display("forma que flanquee' una o varias fichas contrarias.",450,160,self.white,20)
            self.message_display("Las fichas flanqueadas son volteadas para mostrar",450,190,self.white,20)
            self.message_display("el color propio. Es obligatorio voltear todas",450,220,self.white,20)
            self.message_display("las fichas flanqueadas entre la ficha que se coloca",450,250,self.white,20)
            self.message_display("y las que ya estaban colocadas. Una vez",450,280,self.white,20)
            self.message_display("volteadas las fichas el turno pasa al contrario",450,310,self.white,20)
            self.message_display("que procede de la misma forma con sus fichas.",450,340,self.white,20)
            self.message_display("Si un jugador no tiene ninguna posibilidad",450,370,self.white,20)
            self.message_display("de mover, el turno pasa al contrario. La partida",450,400,self.white,20)
            self.message_display("termina cuando ninguno de los dos jugadores",450,430,self.white,20)
            self.message_display("puede mover. Normalmente cuando el tablero",450,460,self.white,20)
            self.message_display("está lleno o prácticamente lleno.Gana el",450,490,self.white,20)
            self.message_display("jugador que acaba con más fichas propias",450,520,self.white,20)
            self.message_display("sobre el tablero Es posible el empate.",450,550,self.white,20)
            self.message_display("Disfruta el Juego",450,600,self.white,40)
            ##
            self.button("Para Volver presione BACKSPACE",290,630,300,50,self.red, self.red, self.black, self.salir)
            pygame.display.update()
            self.win.blit(self.fondo,(0,0))

    #este metodo puede ser mostrar tablero
    def motrar_tablero(self):
        jugar=True
        while jugar:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        jugar = False
                        self.win.blit(self.fondo,(0,0))

            #se muestra el tablero
            self.win.blit(self.fondo,(0,0))
            self.button("Ver Reglas",490,30,150,100,self.bright_blue, self.blue, self.black, self.ver_reglas)
            self.button("Para Volver presione BACKSPACE",490,160,300,100,self.red, self.red, self.black, self.salir)
            self.win.blit(self.board,(30,30))
    		#colocar fichas
            self.win.blit(self.blackToken,((self.cuadro*3)+self.tableroPos+self.borde,(self.cuadro*3)+self.tableroPos+self.borde))
            self.win.blit(self.blackToken,((self.cuadro*4)+self.tableroPos + self.borde,(self.cuadro*4)+self.tableroPos + self.borde))
            self.win.blit(self.whiteToken,((self.cuadro*3)+self.tableroPos+self.borde,(self.cuadro*4)+self.tableroPos+self.borde))
            self.win.blit(self.whiteToken,((self.cuadro*4)+self.tableroPos + self.borde,(self.cuadro*3)+self.tableroPos + self.borde))

            pygame.display.update()

    #falta por definir
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
            self.button("Para Volver presione BACKSPACE",300,500,300,100, self.red, self.red, self.black, self.salir)
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
            self.button("Jugar", 340,400,170,100, self.bright_red, self.red, self.black, self.motrar_tablero)
            pygame.display.update()
            self.clock.tick(15)

        pygame.quit()
