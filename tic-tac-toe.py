
# ---------- Global variables

winner = 0
player = 1
board = []

# ------------ How game looks like in code


def tictactoe_game():
    # print_board(board)
    get_move(board, player)
    # mark(board, player)
    has_won()
    is_full()
    winner = 0
    print_result

#  ---------- Functions --------


def init_board():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    return board


def get_move(board, player):
    row, col = 0, 0
    valid = True
    while valid is True:
        print("Please give row letter: ")
        row_n = input().upper()

        def row_number(row_n):  # convert letter to number
            if row_n == "A":
                row_n = 0
                return(row_n)
            elif row_n == "B":
                row_n = 1
                return(row_n)
            elif row_n == "C":
                row_n = 2
                return(row_n)

        row = row_number(row_n) 
        print("Please give column number: ")  # give col

        try:  # probuje wykonac wprowadzony input i zmienic na int
            col = int(input())-1
        except ValueError:  # podaje jaki blad omijac
            print("Please give right coordinates, eg. A and 1")
            continue  # opusc dalszy kod i wroc do while
        if col not in (0, 1, 2) or row not in (0, 1, 2):
            print("Please give right coordinates, eg. A and 1")
        else:
            valid = False
        
     # ------ dodac funkcje sprawdzajaca czy zajete -----   
    return row, col


board = init_board()
row, col = get_move(board, player)

# def get_ai_move(board, player):
#     """Returns the coordinates of a valid move for player on board."""
#     row, col = 0, 0
#     return row, col


def change_player(player):
    while player == 1:
        mark = "X"
        player = 2
    while player == 2:
        mark = "O"
        player = 1


def mark(board, player, row, col):
    if player == 1:
        board[row][col] = 'X'
        # player = 2
    elif player == 2:
        board[row][col] = 'O'
        # player = 1
    print("After player turn board looks like:  \n",  print_board(board))


def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
    return False


def print_board(board, player=None):
    temp_board = []
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 0:
                temp_board.append('.')
            else:
                temp_board.append(board[i][j])
    print("   1   2   3")
    print("A  {0} | {1} | {2} \n  ---+---+---\n\
B  {3} | {4} | {5} \n  ---+---+---\n\
C  {6} | {7} | {8} \n ".format(temp_board[0], temp_board[1], temp_board[2], temp_board[3], temp_board[4], temp_board[5], temp_board[6], temp_board[7], temp_board[8]))
    pass

mark(board, player, row, col)

   

def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def main_menu():
    tictactoe_game()


if __name__ == '__main__':
    main_menu()
