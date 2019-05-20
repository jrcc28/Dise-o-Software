#from Controlador import Controlador

class Game:
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 0, 0, 0],
            [0, 0, 0, 1, 2, 3, 0, 0],
            [0, 0, 3, 2, 1, 0, 0, 0],
            [0, 0, 0, 3, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]
        #1 es ficha negra
        #2 es ficha blanca
        #si es 3 es que es una posicion valida a poner ficha

    def get_tablero(self):
        return self.board

    def set_ficha(self, fila, columna, valor):
        #solo se permite en posiciones validas
        if self.board[fila][columna] == 3:
            self.board[fila][columna] = valor
            return True
        return False
