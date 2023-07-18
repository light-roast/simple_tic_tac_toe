board = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " +str(board[0][0])+"   |   "+str(board[0][1])+"   |   "+str(board[0][2])+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " +str(board[1][0])+"   |   "+str(board[1][1])+"   |   "+str(board[1][2])+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " +str(board[2][0])+"   |   "+str(board[2][1])+"   |   "+str(board[2][2])+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

print_board(board)

def enter_move(board):
    while True:
        try:
            mov = int(input('Please enter your movement: '))
            if 1 <= mov <= 9:
                found = False
                row_index = None
                column_index = None
                for i, row in enumerate(board):
                    if mov in row:
                        found = True
                        row_index = i
                        column_index = row.index(mov)
                        break

                if found:
                    board[row_index][column_index] = "O"
                    print("Successful movemente at row {row_index} and column {column_index}")
                    return  
                else:
                    print("Invalid movement. Please try again and input a valid location for your movement.")
            else:
                print("Movement should be a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
        

freeFields = []
def make_list_of_free_fields(board):
    #consider delete all the freeFields ant the call of the function
    for i, row in enumerate(board):
        for j, slot in enumerate(row):
            if isinstance(slot, int):
                freeFields.append((i, j))

def victory_for(board, sign):
    
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.


#def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.


#def start_game(board):
    #"hile True:w