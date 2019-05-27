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

    def clean_game(self):
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

                
    def get_tablero(self):
        return self.board

    def hay_posiciones(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 3:
                    return True  
        return False


    def get_estado_juego(self,turno):
        estado = [[0,0,0,0,0]]
        estado[0][0]=self.num_negras
        estado[0][1]=self.num_blancas
        estado[0][2]=turno
        if self.mover_negra:
            estado[0][3]=1
        else:
            estado[0][3]=0

        if self.mover_blanca:
            estado[0][4]=1
        else:
            estado[0][4]=0

        return estado

    def llenar_tablero(self,row,i):
    	for j in range(8):
    	    self.board[i][j]=int(row[j])
           	   
    def llenar_fichas(self,row):
        self.num_negras=int(row[0])
        self.num_blancas=int(row[1])

        if int(row[3])==1:
            self.mover_negra=True
        else:
            self.mover_negra=False

        if int(row[4])==1:
            self.mover_blanca=True
        else:
            self.mover_blanca=0

        return int(row[2])
         
    
    def flip(self, direction, fila,columna, color):
        if direction == 1:
            # north
            row_inc = -1
            col_inc = 0
        elif direction == 2:
            # northeast
            row_inc = -1
            col_inc = 1
        elif direction == 3:
            # east
            row_inc = 0
            col_inc = 1
        elif direction == 4:
            # southeast
            row_inc = 1
            col_inc = 1
        elif direction == 5:
            # south
            row_inc = 1
            col_inc = 0
        elif direction == 6:
            # southwest
            row_inc = 1
            col_inc = -1
        elif direction == 7:
            # west
            row_inc = 0
            col_inc = -1
        elif direction == 8:
            # northwest
            row_inc = -1
            col_inc = -1

        places = []     # pieces to flip
        i = fila + row_inc
        j = columna + col_inc

        if color == 1:
            other = 2
        else:
            other = 1

        if i in range(8) and j in range(8) and self.board[i][j] == other:
            # assures there is at least one piece to flip
            print(1)
            places = places + [(i, j)]
            i = i + row_inc
            j = j + col_inc
            while i in range(8) and j in range(8) and self.board[i][j] == other:
                # search for more pieces to flip
                places = places + [(i, j)]
                i = i + row_inc
                j = j + col_inc
            if i in range(8) and j in range(8) and self.board[i][j] == color:
                # found a piece of the right color to flip the pieces between
                for pos in places:
                    # flips
                    self.board[pos[0]][pos[1]] = color
                    if color == 1:
                        self.num_negras= self.num_negras + 1
                        self.num_blancas= self.num_blancas -1
                    else:
                        self.num_blancas= self.num_blancas + 1
                        self.num_negras= self.num_negras - 1


    def set_ficha(self, fila, columna, valor):
        #solo se permite en posiciones validas
        if self.board[fila][columna] == 3:
            self.board[fila][columna] = valor
            for i in range(1, 9):
                self.flip(i,fila,columna,valor)
            
            if valor==1:
                self.num_negras= self.num_negras + 1
               


            elif valor==2:
                self.num_blancas= self.num_blancas + 1
                 
			
            return True
		
        

        return False
		    
			#calcular posiciones validas aca
			

    def cambiar_turno(self,valor):
        if self.get_valid_moves(valor)==[] and self.num_blancas+self.num_negras==64: 
            if valor==1:
                self.mover_negra=False


            elif valor==2:
                self.mover_blanca=False

            return False

        return True

		
    def escanear_pos(self, fila, columna, color):
        
        if color == 1:
            other = 2
        else:
            other = 1

        places = []

        if (fila < 0 or fila > 7 or columna < 0 or columna > 7):
            return places

   

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
        

        if color == 1:
            other = 2
        else:
            other = 1

        places = []

        for i in range(8):
            for j in range(8):
                if self.board[i][j] == color:
                    places = places + self.escanear_pos(i, j, color)
                if self.board[i][j]==3:
                    self.board[i][j]=0
				    

        places = list(set(places))
		
				
        #print(places)
        for x in places:
            i=int(x[0])
            j=int(x[1])
            self.board[i][j]=3

        return places
		
		
		
		
		
		
        
		
		
		
		
	
