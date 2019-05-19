from Interfaz import Interfaz
from Juego import *

class Controlador:
    def __init__(self,interface,game):
        self.game = game
        self.interfaz = interface

    def start(self):
        self.interfaz.game_menu()


def main():
    interface = Interfaz()
    game = Game()
    controlador = Controlador(interface , game)
    controlador.start()


if __name__ == '__main__':
    main()
