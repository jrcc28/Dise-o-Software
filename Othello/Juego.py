import pygame
import time
pygame.init()

#window
win = pygame.display.set_mode((900, 700))
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
grey=(128,128,128)

#posiciones del tablero
cuadro = 50
borde = 20
tableroPos = 30

#primerJugador, 1 es negra por reglas empieza primero, 2 es blancaas
primero = 1

clock = pygame.time.Clock()

#para mostrar texto
def message_display(text,x,y,color, fontsize):
    largeText = pygame.font.Font('freesansbold.ttf',fontsize)
    TextSurf, TextRect = text_objects(text, largeText,color)
    TextRect.center = (x,y)
    win.blit(TextSurf, TextRect)
    

#para procesar texto
def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def salir():
    return False


def ver_reglas():
    reglas=True
    while reglas:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    reglas = False   
                    win.blit(fondo,(0,0))

        win.blit(fondo,(0,0))
        message_display("El objetivo del juego es tener más fichas del propio color.",450,10,white,20)
        message_display("De inicio se colocan cuatro fichas como en el diagrama.",450,40,white,20)
        message_display("Dos fichas blancas en D4 y E5, y dos negras en E4 y D.",450,70,white,20)
        message_display("Comienzan a mover las negras. Un movimiento consiste",450,100,white,20)
        message_display("en colocar una ficha propia sobre el tablero de",450,130,white,20)
        message_display("forma que flanquee' una o varias fichas contrarias.",450,160,white,20)
        message_display("Las fichas flanqueadas son volteadas para mostrar",450,190,white,20)
        message_display("el color propio. Es obligatorio voltear todas",450,220,white,20)
        message_display("las fichas flanqueadas entre la ficha que se coloca",450,250,white,20)
        message_display("y las que ya estaban colocadas. Una vez",450,280,white,20)
        message_display("volteadas las fichas el turno pasa al contrario",450,310,white,20)
        message_display("que procede de la misma forma con sus fichas.",450,340,white,20)
        message_display("Si un jugador no tiene ninguna posibilidad",450,370,white,20)
        message_display("de mover, el turno pasa al contrario. La partida",450,400,white,20)
        message_display("termina cuando ninguno de los dos jugadores",450,430,white,20)
        message_display("puede mover. Normalmente cuando el tablero",450,460,white,20)
        message_display("está lleno o prácticamente lleno.Gana el",450,490,white,20)
        message_display("jugador que acaba con más fichas propias",450,520,white,20)
        message_display("sobre el tablero Es posible el empate.",450,550,white,20)
        message_display("Disfruta el Juego",450,600,white,40)
        ##
        button("Para Volver presion BACKSPACE",290,630,300,50,red, red, black, salir)
        pygame.display.update()
        win.blit(fondo,(0,0))


#falta mostrar las fichas
def jugar():
    jugar=True
    while jugar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    jugar = False   
                    win.blit(fondo,(0,0))

        #se muestra el tablero
        win.blit(fondo,(0,0))
        button("Ver Reglas",490,30,150,100,bright_blue, blue, black, ver_reglas)
        button("Para Volver presion BACKSPACE",490,160,300,100,red, red, black, salir)
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
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    escoger = False   
                    win.blit(fondo,(0,0))	
			
        win.blit(fondo,(0,0))
        button("Para Volver presion BACKSPACE",300,500,300,100, red, red, black, salir)
        button("Negras",340,300,170,100, bright_black, grey ,white, elegir_negras)
        button("Blancas", 340,100,170,100, bright_white, white ,black, elegir_blancas)
        pygame.display.update()
			
        


def elegir_blancas():
    primero = 2
    win.blit(fondo,(0,0))
    message_display("                                           El jugador ha escogido las fichas blancas.",(300),(500/2),white,30)
    pygame.display.update()
    time.sleep(2)
    
	
def elegir_negras():
	primero = 1
	win.blit(fondo,(0,0))
	message_display("                                           El jugador ha escogido las fichas negras.",(300),(500/2),white,30)
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
    message_display(msg,(x+(w/2)),(y+(h/2)),color3,17)
    #clock.tick(15)
    


#menu del juego
def game_menu(): 
    intro=True   
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               intro = False
  
        win.blit(fondo,(0,0))

        message_display("OTHELLO",(900/2),(500/2),white,100)

        #botones de las opciones
        button("Ver Reglas",640,400,170,100, bright_blue, blue, black, ver_reglas)
        button("Elegir Color",40,400,170,100, bright_green, green,black, elegir_color)
        button("Jugar", 340,400,170,100, bright_red, red, black, jugar)
        pygame.display.update()
        clock.tick(15)
    
 


game_menu() 
pygame.quit()