import random

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
                        print(f'Successful movemente at row {row_index} and column {column_index}')
                        return  
                    else:
                        print("Invalid movement. Please try again and input a valid location for your movement.")
                        continue
                else:
                    print("Movement should be a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        
        


def make_list_of_free_fields(board):
    free_slots = []
    for i, row in enumerate(board):
        for j, slot in enumerate(row):
            if isinstance(slot, int):
                free_slots.append((i, j))
    return free_slots


def victory_for(board, sign):
    if sign == "X":
        who = "me"
    elif sign == "O":
        who = "you"
    else:
        who = None
    cross1 = cross2 = True
    for check in range(3):
        if board[check][0] == sign and board[check][1] == sign and board[check][2] == sign:
            return who
        if board[0][check] == sign and board[1][check] == sign and board[2][check] == sign:
            return who
        if board[check][check] != sign:
            cross1 = False
        if board[check][2-check] != sign: 
            cross2 = False
    if cross1 or cross2:
        return who
    return None



def draw_move(board):
    free_slots = make_list_of_free_fields(board)
    ran_choice = random.choice(free_slots)
    board[ran_choice[0]][ran_choice[1]] = "X"
    display_board(board)
    


def start_game(board):
    display_board(board)
    draw_move(board)
    victory = None
    turn = True
    while victory is None:
        if turn:
            enter_move(board)
            victory = victory_for(board, 'O')
            turn = False
            print("My turn")
        else:
            draw_move(board)
            victory = victory_for(board, 'X')
            turn = True
            print("Your turn")

    if victory == "me":
            print("Nope! I win!")
            display_board(board)
            return
    elif victory == "you":
            print("Amm... You win!")
            display_board(board)
            return
    elif victory is None and len(make_list_of_free_fields(board)) == 0:
            print("No... It's a draw!")
            display_board(board)
            return
    

start_game(board)        
