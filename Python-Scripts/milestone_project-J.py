def display_board(board):
    result = ''
    tbl = { 'line1':'   |   |   \n', 'area7':'   ', 'line2-1':'|', 'area8':'   ', 'line2-2':'|', 'area9':'   ', 'line2-3':'\n', 'line3':'   |   |   \n', 'line4':'-----------\n', 'line5':'   |   |   \n', 'area4':'   ', 'line6-1':'|', 'area5':'   ', 'line6-2':'|', 'area6':'   ', 'line6-3':'\n', 
            'line7':'   |   |   \n', 'line8':'-----------\n', 'line9':'   |   |   \n', 'area1':'   ', 'line10-1':'|', 'area2':'   ', 'line10-2':'|', 'area3':'   ', 'line10-3':'\n', 'line11':'   |   |   \n' }

    for num in range(1,10):
        tbl['area' + str(num)] = ' ' + board[num] + ' '

    for i,j in tbl.items():
        result += tbl[i]
    
    return print(result)

import random

def choose_first():
    items = ['Player1', 'Player2']
    return random.choice(items)

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for space in board:
        if space == ' ':
            result = True
            break
        else:
            result = False
    return result

def player_input():
    first_marker = ' '
    while first_marker.upper() != 'X' and first_marker.upper() != 'O':
        first_marker = input("Do you want to be 'X' or 'O' ").upper()
    
    marker1 = first_marker
    if marker1 == 'X':
        marker2 = 'O'
    else:
        marker2 = 'X'
    return (marker1, marker2)

def place_marker(board, marker, position):
    board[position] = marker
    
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
    while True:
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
  
first_player = ''
next_player = ''
marker = ''
game_on = bool()

while True:
    first_player = choose_first()
    print(f'{first_player} will go first.\n')

    if first_player == 'Player1':
        next_player = 'Player2'
        marker = player_input()
    else:
        first_player = 'Player2'
        next_player = 'Player1'
        marker = player_input()

    ready = input('Are you ready to play? Enter Yes or No. ')
    if ready.lower() == 'yes' or ready.lower() == 'y':
        game_on = True
    else:
        game_on = False
        break
    play_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(play_board)
    
    while game_on:
        print(f'\n{first_player}:', end=" ")
        position1 = player_choice(play_board)
        available1 = space_check(play_board,position1)

        while not available1:
            position1 = player_choice(play_board)
            available1 = space_check(play_board,position1)
        place_marker(play_board,marker[0],position1)
        display_board(play_board)
        we_have_a_winner = win_check(play_board,marker[0])
        
        if we_have_a_winner == True:
            print(f'\nCongratulations {first_player}! You have won the game!')
            break
        game_on = full_board_check(play_board)
        
        if game_on == False:
            print('The game is a draw!')
            break
        print(f'\n{next_player}:', end=" ")
        position2 = player_choice(play_board)
        available2 = space_check(play_board,position2)
        
        while not available2:
            position2 = player_choice(play_board)
            available2 = space_check(play_board,position2)
        place_marker(play_board,marker[1],position2)
        display_board(play_board)
        we_have_a_winner = win_check(play_board,marker[1])
        
        if we_have_a_winner == True:
            print(f'\nCongratulations {next_player}! You have won the game!')
            break
        game_on = full_board_check(play_board)
        
        if game_on == False:
            print('The game is a draw!')
            break
        
    if not replay():
        break