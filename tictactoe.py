import math 

class TicTacToe():
    def __init__(self, board, cross):
        self.board = board
        self.cross = cross

    def genmoves(self, board, cross):
        """ Generador de movimientos posibles de un tablero """
        moves = []
        for i in range(0,8):
            newboard = board.copy()
            if(newboard[i] == ' '):
                if cross:
                    newboard[i] = 'x'
                    moves.append(newboard)
                else:
                    newboard[i] = 'o'
                    moves.append(newboard)
        return moves
        
    def won(self, board): 
        """ Determina si un tablero ya se ha ganado """
        for i in range(0,3):
            if board[3*i] == board[3*i+1] and board[3*i+1]  == board[3*i+2] and board[3*i+2] != ' ':
                return True
            if board[i] == board[i+3] and board[i+3] == board[i+6] and board[i+6] != ' ':
                return True
        if board[0] == board[4] and board[4] == board[8] and board[8] != ' ':
            return True
        if board[2] == board[4] and board[4] == board[6] and board[6] != ' ':
            return True

        return False

    def printBoard(self, board):
        """ Formato para imprimir tablero """
        for x in range(0,3):
            if x % 3 == 0:
                print()
            
            print(board[3*x],"|", board[3*x+1], "|", board[3*x+2])
    
    def winPossibility(self, board, cross):
        """ Posibilidad de que un tablero se pueda ganar aun por un jugador """
        # Número de filas, columnas o diagonales que aún se pueden ganar
        contador = 0
        if cross:
            var = 'o'
        else:
            var = 'x'
        for i in range(0,3):
            if board[3*i] != var and board[3*i + 1] != var and board[3*i + 2] != var:
                contador = contador + 1
            if board[i] != var and board[i+3] != var and board[i+6] != var:
                contador = contador + 1
        if board[0] != var and board[4] != var and board[8] != var:
            contador = contador + 1
        if board[2] != var and board[4] != var and board[6] != var:
            contador = contador + 1

        return contador
        
    def alphabeta(self, move, alpha, beta, maxplayer):

        # Si ya no se pueden generar movimientos o ya se ganó algún tablero

        if len(self.genmoves(move, self.cross)) == 0 or self.won(move):
            if maxplayer:
                if(self.won(move)): #Si ya ganó la persona cuando sea turno de la máquina
                    return -1000
                else:
                    return(self.winPossibility(move,not(maxplayer))-self.winPossibility(move,maxplayer)) #Si no determina el nivel de posibilidad para ganar aún
            else:
                if(self.won(move)): #Si ya ganó la máquina cuando es turno de la persona
                    return 1000
                else:
                    return(self.winPossibility(move,maxplayer)-self.winPossibility(move, not(maxplayer))) #Si no calcula la posibilidad de que gane la persona

        if maxplayer:
            moves = self.genmoves(move,not(self.cross)) 
        else:
            moves = self.genmoves(move, self.cross)
            
        if maxplayer:
            val = -math.inf
            for move in moves:
                val = max(val, self.alphabeta(move, alpha, beta, False)) #
                alpha = max(alpha, val)
                if alpha >= beta:
                    break
            return val
        else:
            val = math.inf
            for move in moves:
                val = min(val, self.alphabeta(move, alpha, beta, True)) 
                beta = min(beta, val)
                if alpha >= beta:
                    break
            return val

    def tttplayer(self):
        print("------------- Tic Tac Toe ----------")
        if self.cross:
            print("Tu ficha: x")
        else:
            print("Tu ficha: o")

        while True:
            self.printBoard(self.board)

            while True:
                xy = input("Tu turno. Coordenada: ")
                casilla =  eval(xy)[0]*3 + eval(xy)[1]
                if casilla >= 0 and casilla < 9 and self.board[casilla] == ' ':
                    if self.cross:
                        self.board[casilla] = 'x'
                    else:
                        self.board[casilla] = 'o'
                    break
                else:
                    print("----------- Invalid move")

            #Revisa si con la última jugada de la persona se ganó
            if self.won(self.board):
                self.printBoard(self.board)
                print("----------- ¡¡¡Ganaste!!!")
                break
            
            score = []
            moves = self.genmoves(self.board, not(self.cross))

            #Si ya no se pueden generar jugadas y nadie ha ganado es empate
            if len(moves) == 0:
                self.printBoard(self.board)
                print("----------- Empate")
                break

            for move in moves:
                score.append((move, self.alphabeta(move, -math.inf, math.inf, False)))

            m = sorted(score, key=lambda res:res[1])
            self.board = m[-1][0]
            
            #Despues del movimiento de la máquina determina si ya ganó
            if self.won(self.board):
                self.printBoard(self.board)
                print("----------- Ganó Cortana")
                break

            #Si no ha ganado, determina si hay empate
            moves = self.genmoves(self.board, self.cross)
            if len(moves) == 0:
                self.printBoard(self.board)
                print("----------- Empate")
                break


board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
#TicTacToe([tablero inicial], [x -> True, o -> False])
ttt = TicTacToe(board, True)
#Comienza el juego
ttt.tttplayer()

