# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going
game_still_going = True

# Winner or tie
winner = None

# Whose turn is it
current_player = "X"


def display_board():
    # Creation of initial board
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i+1] + " | " + board[i+2])


def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    # Check if you entered correct position on board
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
        position = int(position) - 1
        if board[position] == '-':
            valid = True
        else:
            print("Enter empty space.")
    board[position] = player
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    # If any row has 3 matches
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    global game_still_going
    col_1 = board[0] == board[3] == board[6] != '-'
    col_2 = board[1] == board[4] == board[7] != '-'
    col_3 = board[2] == board[5] == board[8] != '-'
    # If any column has 3 matches
    if col_1 or col_2 or col_3:
        game_still_going = False
    # Return winner
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def check_diagonals():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[2] == board[4] == board[6] != '-'
    # If any row has 3 matches
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return


def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False
    return


def flip_player():
    global current_player
    # Flip current player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return


def game():
    # Display initial board
    display_board()
    # Play game while there is no winner or no draw
    while game_still_going:
        # Handle current players turn
        handle_turn(current_player)
        # Check if game has ended
        check_if_game_over()
        # Switch between players
        flip_player()
    # Game has ended
    if winner == "X" or winner == "O":
        print("Winner is " + winner)
    elif winner == None:
        print("It's a tie.")


game()
