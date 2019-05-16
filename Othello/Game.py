import pygame
import time
pygame.init()

#window
win = pygame.display.set_mode((610, 610))
pygame.display.set_caption("OTHELLO")

#sprites
fondo = pygame.image.load('fondo.jpg')
board = pygame.image.load('board.bmp')
whiteToken = pygame.image.load('blanca.bmp')
blackToken = pygame.image.load('negra.bmp')

#colores
white=(255,255,255)
black = (0,0,0)  
red = (200,0,0)
green = (0,200,0)
blue=(0, 0, 200)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue=(0, 0, 255)
bright_white=(200, 200, 200)
bright_black=(70,70,70)

#posiciones del tablero
cuadro = 50
borde = 20
tableroPos = 30

#primerJugador, 1 es negra por reglas empieza primero, 2 es blancaas
primero = 1

clock = pygame.time.Clock()

#para mostrar texto
def message_display(text,y, color):
    largeText = pygame.font.Font('freesansbold.ttf',15)
    TextSurf, TextRect = text_objects(text, largeText,color)
    TextRect.center = (210,y)
    win.blit(TextSurf, TextRect)
    

#para procesar texto
def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def ver_reglas():
    reglas=True
    while reglas:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               reglas = False
			   
        win.blit(fondo,(0,0))
        message_display("El objetivo del juego es tener más fichas del propio color.",10,white)
        message_display("De inicio se colocan cuatro fichas como en el diagrama.",30,white)
        message_display("Dos fichas blancas en D4 y E5, y dos negras en E4 y D5.",50,white)
        message_display("Comienzan a mover las negras. Un movimiento consiste",70,white)
        message_display("en colocar una ficha propia sobre el tablero de",90,white)
        message_display("forma que flanquee' una o varias fichas contrarias.",110,white)
        message_display("Las fichas flanqueadas son volteadas para mostrar",130,white)
        message_display("el color propio. Es obligatorio voltear todas",150,white)
        message_display("las fichas flanqueadas entre la ficha que se coloca",170,white)
        message_display("y las que ya estaban colocadas. Una vez",190,white)
        message_display("volteadas las fichas el turno pasa al contrario",210,white)
        message_display("que procede de la misma forma con sus fichas.",230,white)
        message_display("Si un jugador no tiene ninguna posibilidad",250,white)
        message_display("de mover, el turno pasa al contrario. La partida",270,white)
        message_display("termina cuando ninguno de los dos jugadores",290,white)
        message_display("puede mover. Normalmente cuando el tablero",310,white)
        message_display("está lleno o prácticamente lleno.Gana el",330,white)
        message_display("jugador que acaba con más fichas propias",350,white)
        message_display("sobre el tablero Es posible el empate.",370,white)
        
        pygame.display.update()
        win.blit(fondo,(0,0))


#falta mostrar las fichas
def jugar():
    jugar=True
    while jugar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               jugar = False
               win.blit(fondo,(0,0))
			   
			   
        #se muestra el tablero
        button("Ver Reglas",490,30,100,50,bright_white,white,black,ver_reglas)
        win.blit(board,(30,30))
		#colocar fichas
        win.blit(blackToken,((cuadro*3)+tableroPos+borde,(cuadro*3)+tableroPos+borde))
        win.blit(blackToken,((cuadro*4)+tableroPos + borde,(cuadro*4)+tableroPos + borde))
        win.blit(whiteToken,((cuadro*3)+tableroPos+borde,(cuadro*4)+tableroPos+borde))
        win.blit(whiteToken,((cuadro*4)+tableroPos + borde,(cuadro*3)+tableroPos + borde))
		
        pygame.display.update()
		
		

#falta por definir
def elegir_color():
    escoger=True
    while escoger:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                escoger = False   
                win.blit(fondo,(0,0))	
			
        win.blit(fondo,(0,0))
        button("Negras", 190,300,100,50, bright_black, black ,white, elegir_negras)
        button("Blancas", 310,300,100,50, bright_white, white ,black, elegir_blancas)
        pygame.display.update()
			
        


def elegir_blancas():
    primero = 2
    win.blit(fondo,(0,0))
    message_display("                                           El jugador ha escogido las fichas blancas.",370,white)
    pygame.display.update()
    time.sleep(2)
    
	
def elegir_negras():
	primero = 1
	win.blit(fondo,(0,0))
	message_display("                                           El jugador ha escogido las fichas negras.",370,white)
	pygame.display.update()
	time.sleep(2)
	
	
#metodo del boton donde 
#msg es el texto del boton
#x y w h son las cordenadas del boton x,y, height y width
#color1 es el color del boton cuando se selecciona
#color2 es el color cuando no se toca
#color3 es el color del texto 
#action es el objeto del metodo que ejecuta el boton
def button(msg,x,y,w,h,color1,color2,color3, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #si el mouse esta encima del boton cambia de color
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win, color1,(x,y,w,h))
         
        #click se ejecuta el metodo
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(win, color2,(x,y,w,h))
 
    #texto del boton
    smallText = pygame.font.Font("freesansbold.ttf",17)
    textSurf, textRect = text_objects(msg, smallText, color3)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    win.blit(textSurf, textRect)
    #clock.tick(15)
    


#menu del juego
def game_menu(): 
    intro=True   
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               intro = False
  
        win.blit(fondo,(0,0)) 

        largeText = pygame.font.Font('freesansbold.ttf',60)
        TextSurf, TextRect = text_objects("OTHELLO", largeText, red)
        TextRect.center = ((450/2),(450/2))
        win.blit(TextSurf, TextRect) 
   

        #botones de las opciones
        button("Ver Reglas", 300,300,100,50, bright_blue, blue, black, ver_reglas)
		#este boton de escoger boton es mas para el framework no para este juego
        button("Elegir Color", 40,300,100,50, bright_green, green,black, elegir_color)
        button("Jugar", 170,300,100,50, bright_red, red, black, jugar)
        pygame.display.update()
        clock.tick(15)
    
 


game_menu() 
pygame.quit()