from Interfaz import *
from Juego import *

class Controlador:
    def __init__(self):
        self.game = Game()
        self.interfaz = Interfaz(self)

    def start(self):
        self.interfaz.game_menu()

    def get_tablero(self):
        return self.game.get_tablero()

    def set_ficha(self, x , y , valor):
        return self.game.set_ficha(x,y,valor)

def main():
    controlador = Controlador()
    controlador.start()


if __name__ == '__main__':
    main()
