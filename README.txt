# Tic Tac Toe

Inteligencia Artificial

-------------- Alan Antonio Alvarez Sánchez

Para inicar el juego se debe de editar el archivo tictactoe.py. Dentro del mismo, hasta el final, se encuentra una lista llamada tablero que contiene el tablero inicial. 

board = [' ', ' ', ' ', ' ', ' ', ' ',' ', ' ',' ']

Board contiene 9 casillas dentro de las cuales debe ir: 'x', 'o', ó ' '. Cabe mencionar que las letras deben de ser en minusculas. 

Una vez definido el tablero inicial se procede a crear una variable de tipo TicTacToe() la cual recibe dos parámetros: el tablero inicial y si el jugador comienza con 'x' u 'o'.

ttt = TicTacToe(board, True) -> True: 'x', False: 'o'

Despues se manda a llamar al método tttplayer() que es quien comienza el juego.

Una vez inicializado el juego el usuario deberá ingresar progresivamente las coordenadas donde desea colocar una ficha en su turno. Dichas coordanadas pueden ser ingresadas de estas dos maneras: (1,1) ó 1,1.

Ejemplo:

(prompt)Tu turno. Coordenadas: (1,1)
(prompt)Tu turno. Coordenadas: 1,1

Continuar jugando hasta que logre vencer a la máquina, si puede.