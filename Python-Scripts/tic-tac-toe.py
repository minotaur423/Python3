# Function that prints out a board
# from IPython.display import clear_output
def display_board(board):
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
def player_input():
    player1 = input("Please pick a marker 'X' or 'O': ")
    if player1.lower() == 'x':
        marker = 'X'
        print(f'Player1 is {marker} and Player2 is O.')
    else:
        marker = 'O'
        print(f'Player1 is {marker} and Player2 is X.')
    return marker

# Function takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    test_board[position] = marker

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
    for i in range(len(board)):
        if board[i] == " ":
            return False
        else:
            return True

# Function asks player if they want to play again; returns a boolean True if yes.
def replay():
    replay = input('Would you like to play again? (Y/n)')
    if replay.lower() == 'y':
        return True
    else:
        return False

# Function asks for player's next position and then uses function from step 6 to check if it's a free position. If it is, then return the position for later use.
def player_choice(board):
    position = int(input('Please enter a number: '))
    if space_check(board,position) == True:
        return position
    else:
        return 'Space used.'
    
test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

play = player_input()

slot = int(input('Please enter a number: '))

place_marker(test_board,play,slot)
display_board(test_board)