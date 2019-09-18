# Step 1: Function that prints out a board
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

# Step 2: Function takes in player input and assigns marker as 'X' or 'O'
def player_input():
    '''
    OUTPUT = (Player1 marker, Player 2 marker)
    '''
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player1: Choose X or O: ").upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Step 3: Function takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    board[position] = marker

# Step 4: Function takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or 
    (board[4] == board[5] == board[6] == mark) or 
    (board[7] == board[8] == board[9] == mark) or 
    (board[1] == board[4] == board[7] == mark) or 
    (board[2] == board[5] == board[8] == mark) or 
    (board[3] == board[6] == board[9] == mark) or 
    (board[1] == board[5] == board[9] == mark) or 
    (board[3] == board[5] == board[7] == mark))
    
# Step 5: Function to select the first player.
from random import randint

def choose_first():

    flip = randint(0,1)
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"

# Step 6: Function returns a boolean indicating whether a space on the board is available.
def space_check(board, position):
    return board[position] == ' '

# Step 7: Function checks if the board is full and returns True if full, False otherwise.
def full_board_check(board):

    if " " in board[1:]:
        return False
    else:
        # Board is full
        return True

# Step 8: Function asks for player's next position and then uses function from step 6 to check if it's a free position. If it is, then return the position for later use.
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('\nPlease enter a number (1-9): '))

    return position

# Step 9: Function asks player if they want to play again; returns a boolean True if yes.
def replay():
    restart = input('\nPlay again? Enter Yes or No ')

    return restart == 'Yes'


print("Welcome to Tic Tac Toe!\n")

while True:
    test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to play? y or n? ')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        
        if turn == 'Player 1':
            # Player 1 turn.
            # Show the board
            display_board(test_board)
            
            # Choose the position
            position = player_choice(test_board)
            
            # Place the marker on the position
            place_marker(test_board, player1_marker,position)
            
            # Check if they won
            if win_check(test_board,player1_marker):
                display_board(test_board)
                print('PLAYER 1 HAS WON!!!')
                game_on = False
            # Or, check if there is a tie. # No tie and no win?  The next player's turn.
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            # Player 2 turn.
            # Show the board
            display_board(test_board)
            
            # Choose the position
            position = player_choice(test_board)
            
            # Place the marker on the position
            place_marker(test_board, player2_marker,position)
            
            # Check if they won
            if win_check(test_board,player2_marker):
                display_board(test_board)
                print('PLAYER 2 HAS WON!!!')
                game_on = False
            # Or, check if there is a tie. No tie and no win? The next player's turn.
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 1'
    
    if not replay():
        break
    else:
        continue