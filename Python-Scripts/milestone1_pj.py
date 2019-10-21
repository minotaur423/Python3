def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

import random

def choose_first():
    players = ['Player1', 'Player2']
    return random.choice(players)

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    if ' ' not in board[1:]:
        return False
    else:
        return True

def player_input():
    mark = ' '
    while mark.upper() != 'X' and mark.upper() != 'O':
        mark = input("Do you want to be 'X' or 'O' ")
    
    mark1 = mark.upper()
    if mark1 == 'X':
        mark2 = 'O'
    else:
        mark2 = 'X'
    return (mark1, mark2)

def place_marker(board, mark, position):
    board[position] = mark
    
def win_check(board, mark):
    win = [mark]*3
    if board[1:4] == win or board[4:7] == win or board[7:] == win:
        result = True
    elif board[1:8:3] == win or board[2:9:3] == win or board[3::3] == win:
        result = True
    elif board[1::4] == win or board[3:8:2] == win:
        result = True
    else:
        result = False
    
    return result

def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board,position):
        try:
            position = int(input('Please enter a number from 1-9: '))
            if position > 9 or position < 0:
                print("\nYou must enter a number from 1 to 9: ")
                continue
        except ValueError:
            print("\nYou must enter a number from 1 to 9: ")
            continue
        else:
            break
    return position
        
def replay():
    play_again = input('\nDo you want to play again? Enter Yes or No: ')
    if play_again.upper() == 'YES' or play_again.upper() == 'Y':
        return True
    else:
        return False
    
print('Welcome to Tic Tac Toe!\n')
  
turn = ''
next_turn = ''
marker = ''
game_on = bool()

while True:
    # Select first player.
    turn = choose_first()
    print(f'{turn} will go first.\n')
    
    # Conditional statement to designate Player1 and Player2 and each's mark.
    if turn == 'Player1':
        next_turn = 'Player2'
        marker = player_input()
    else:
        turn = 'Player2'
        next_turn = 'Player1'
        marker = player_input()
        
    # Confirm player is ready to start game.
    ready = input('Are you ready to play? Enter Yes or No. ')
    if ready.lower() == 'yes' or ready.lower() == 'y':
        game_on = True
    else:
        break
    
    # Construct the board and display
    play_board = [' '] * 10
    display_board(play_board)

    # Start game loop.
    while game_on:
        # First player's turn.
        print(f'\n{turn}:', end=" ")
        # Take input from first player and place mark on board.
        position1 = player_choice(play_board)
        place_marker(play_board,marker[0],position1)
        # Display the board with the first player's mark.
        display_board(play_board)
        # Check if there is a winner.
        we_have_a_winner = win_check(play_board,marker[0])
        if we_have_a_winner == True:
            print(f'\nCongratulations {turn}! You have won the game!')
            break
        # Check if the board is full and declare a draw if this is the case.
        game_on = full_board_check(play_board)
        if game_on == False:
            print('The game is a draw!')
            break
        
        # Second player's turn.
        print(f'\n{next_turn}:', end=" ")
        # Take input from first player and place mark on board.
        position2 = player_choice(play_board)
        place_marker(play_board,marker[1],position2)
        # Display the board with the first player's mark.
        display_board(play_board)
        # Check if there is a winner.
        we_have_a_winner = win_check(play_board,marker[1])
        if we_have_a_winner == True:
            print(f'\nCongratulations {next_turn}! You have won the game!')
            break
        # Check if the board is full and declare a draw if this is the case.
        game_on = full_board_check(play_board)
        if game_on == False:
            print('The game is a draw!')
            break
    # Play new game if player selects yes.     
    if not replay():
        break