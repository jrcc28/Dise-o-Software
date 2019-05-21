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
        self.mover_negra=True
        self.mover_blanca=True
        self.num_negras=2
        self.num_blancas=2
        #1 es ficha negra
        #2 es ficha blanca
        #si es 3 es que es una posicion valida a poner ficha

    def get_num_negras(self):
        return self.num_negras

    def get_num_blancas(self):
        return self.num_blancas

    def get_mover_negras(self):
        return self.mover_negra

    def get_mover_blancas(self):
        return self.mover_blanca


    def get_tablero(self):
        return self.board

    def hay_posiciones(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 3:
                    print(self.board)
                    return True
        print(self.board)
        return False



    def set_ficha(self, fila, columna, valor):
        #solo se permite en posiciones validas
  
        if self.board[fila][columna] == 3:
            self.board[fila][columna] = valor
            if valor==2:
                self.num_negras= self.num_negras + 1


            elif valor==1:
                self.num_blancas= self.num_blancas + 1     
			
            return True
		
        

        return False
		    
			#calcular posiciones validas aca
			

    def cambiar_turno(self,valor):
        if self.get_valid_moves(valor)==[] and self.num_blancas+self.num_negras==64: 
            if valor==2:
                self.mover_negra=False


            elif valor==1:
                self.mover_blanca=False

            return False

        return True

		
    def lookup(self, fila, columna, color):
        """Returns the possible positions that there exists at least one
        straight (horizontal, vertical, or diagonal) line between the
        piece specified by (fila, columna, color) and another piece of
        the same color.
        """
        if color == 1:
            other = 2
        else:
            other = 1

        places = []

        if (fila < 0 or fila > 7 or columna < 0 or columna > 7):
            return places

    # For each direction search for possible positions to put a piece.

        # north
        i = fila - 1
        if (i >= 0 and self.board[i][columna] == other):
            i = i - 1
            while (i >= 0 and self.board[i][columna] == other):
                i = i - 1
            if (i >= 0 and self.board[i][columna] == 0):
                places = places + [(i, columna)]

        # northeast
        i = fila - 1
        j = columna + 1
        if (i >= 0 and j < 8 and self.board[i][j] == other):
            i = i - 1
            j = j + 1
            while (i >= 0 and j < 8 and self.board[i][j] == other):
                i = i - 1
                j = j + 1
            if (i >= 0 and j < 8 and self.board[i][j] == 0):
                places = places + [(i, j)]

        # east
        j = columna + 1
        if (j < 8 and self.board[fila][j] == other):
            j = j + 1
            while (j < 8 and self.board[fila][j] == other):
                j = j + 1
            if (j < 8 and self.board[fila][j] == 0):
                places = places + [(fila, j)]

        # southeast
        i = fila + 1
        j = columna + 1
        if (i < 8 and j < 8 and self.board[i][j] == other):
            i = i + 1
            j = j + 1
            while (i < 8 and j < 8 and self.board[i][j] == other):
                i = i + 1
                j = j + 1
            if (i < 8 and j < 8 and self.board[i][j] == 0):
                places = places + [(i, j)]

        # south
        i = fila + 1
        if (i < 8 and self.board[i][columna] == other):
            i = i + 1
            while (i < 8 and self.board[i][columna] == other):
                i = i + 1
            if (i < 8 and self.board[i][columna] == 0):
                places = places + [(i, columna)]

        # southwest
        i = fila + 1
        j = columna - 1
        if (i < 8 and j >= 0 and self.board[i][j] == other):
            i = i + 1
            j = j - 1
            while (i < 8 and j >= 0 and self.board[i][j] == other):
                i = i + 1
                j = j - 1
            if (i < 8 and j >= 0 and self.board[i][j] == 0):
                places = places + [(i, j)]

        # west
        j = columna - 1
        if (j >= 0 and self.board[fila][j] == other):
            j = j - 1
            while (j >= 0 and self.board[fila][j] == other):
                j = j - 1
            if (j >= 0 and self.board[fila][j] == 0):
                places = places + [(fila, j)]

        # northwest
        i = fila - 1
        j = columna - 1
        if (i >= 0 and j >= 0 and self.board[i][j] == other):
            i = i - 1
            j = j - 1
            while (i >= 0 and j >= 0 and self.board[i][j] == other):
                i = i - 1
                j = j - 1
            if (i >= 0 and j >= 0 and self.board[i][j] == 0):
                places = places + [(i, j)]

        return places
		
		
    def get_valid_moves(self, color):
        """Get the avaiable positions to put a piece of the given color. For
        each piece of the given color we search its neighbours,
        searching for pieces of the other color to determine if is
        possible to make a move. This method must be called before
        apply_move.
        """

        if color == 1:
            other = 2
        else:
            other = 1

        places = []

        for i in range(8):
            for j in range(8):
                if self.board[i][j] == color:
                    places = places + self.lookup(i, j, color)
                if self.board[i][j]==3:
                    self.board[i][j]=0
				    

        places = list(set(places))
		
				
        #print(places)
        for x in places:
            i=int(x[0])
            j=int(x[1])
            self.board[i][j]=3

        return places
		
		
		
		
		
		
        
		
		
		
		
	
