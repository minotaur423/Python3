# Function that prints out a board
# from IPython.display import clear_output

def display_board(board):
#    clear_output()  # Remember, this only works in jupyter!

    print(f'      |       |      ')
    print(f'  {board[7]}   |   {board[8]}   |   {board[9]}  ')
    print(f'      |       |      ')
    print('- - - - - - - - - - -')
    print(f'      |       |      ')
    print(f'  {board[4]}   |   {board[5]}   |   {board[6]}  ')
    print(f'      |       |      ')
    print('- - - - - - - - - - -')
    print(f'      |       |      ')
    print(f'  {board[1]}   |   {board[2]}   |   {board[3]}  ')
    print(f'      |       |      ')

# Function takes in player input and assigns marker as 'X' or 'O'
def player_input(player):
    marker = ''
    while not marker:
        marker = input("Please pick a marker 'X' or 'O': ")
        if player == 1 and marker.lower() == 'x':
            marker = 'X'
            print('\n' + f'Player1 is X and Player2 is O.')
        elif player == 1 and marker.lower() == 'o':
            marker = 'O'
            print('\n' + f'Player1 is O and Player2 is X.')
        elif player == 2 and marker.lower() == 'x':
            marker = 'X'
            print('\n' + f'Player2 is X and Player1 is O.')
        elif player == 2 and marker.lower() == 'o':
            marker = 'O'
            print('\n' + f'Player2 is O and Player1 is X.')
        else:
            print('\n' + f'Your selection "{marker}" is not valid.\n')
            marker = ''
    return marker

# Function takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    board[position] = marker

# Function takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False
    
# Function returns a boolean indicating whether a space on the board is available.
def space_check(board, position):
    return board[position] == ' '

# Function checks if the board is full and returns True if full, False otherwise.
def full_board_check(board):
    result = True
    for i in range(len(board)):
        if board[i] == " ":
            result = False
    return result

# Function asks player if they want to play again; returns a boolean True if yes.
def replay():
    restart = input('\nWould you like to play again? (Y/n)')
    if restart.lower() == 'y':
        return True
    else:
        return False

# Function asks for player's next position and then uses function from step 6 to check if it's a free position. If it is, then return the position for later use.
def player_choice(board):
    position = ''
    while not position:
        while True:
            try:
                position = int(input('\nPlease enter a number: '))
            except:
                print(f'Your entry is not a number from 1 to 9.')
                continue
            else:
                break
        if space_check(board,position) == True:
            return position
        else:
            print('The number select has been used. Pick another number.')
            position = ''

# Function to select the first player.
from random import randint

def choose_first():
    player1 = 1
    player2 = 2
    player = randint(player1,player2)
    return player


while True:
    test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    game_on = True

    print("Welcome to Tic Tac Toe!\n")

    # The function will select the first player.
    first_player = choose_first()
    if first_player == 1:
        second_player = 2
        print(f'Player1 will go first.'+'\n')
        # This function will return a marker for the first player.
        marker_selected = player_input(first_player)
        if marker_selected == 'X':
            first = 'X'
            second = 'O'
        else:
            second = 'X'
            first = 'O'
    else:
        second_player = 1
        print(f'Player2 will go first.'+'\n')
        # This function will return a marker for the first player.
        marker_selected = player_input(first_player)
        if marker_selected == 'X':
            first = 'X'
            second = 'O'
        else:
            second = 'X'
            first = 'O'

    while game_on:
        #Player 1 Turn
        slot = int(player_choice(test_board))
        place_marker(test_board,first,slot)
        display_board(test_board)
        if  win_check(test_board, first) == True:
            print('\n' + f'Player{first_player} wins!!!')
            game_on = False
            break
        elif full_board_check(test_board) == True:
            print('\nThis game is a draw!!!')
            game_on = False
            break
        
        # Player2's turn.
        slot = int(player_choice(test_board))
        place_marker(test_board,second,slot)
        display_board(test_board)
        if  win_check(test_board, second) == True:
            print('\n' + f'Player{second_player} wins!!!')
            game_on = False
            break
        elif full_board_check(test_board) == True:
            print('\nThis game is a draw!!!')
            game_on = False
            break

    if not replay():
        break
    else:
        continue