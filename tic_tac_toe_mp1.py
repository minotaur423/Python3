def display_board(board):
    print(" " + " " + " " + "|" + " " + " " + " " + "|" + " " + " " + " ")
    print(" " + board[7] + " " + "|" + " " + board[8] + " " + "|" + " " + board[9] + " ")
    print(" " + " " + " " + "|" + " " + " " + " " + "|" + " " + " " + " ")
    print("------------")
    print(" " + " " + " " + "|" + " " + " " + " " + "|" + " " + " " + " ")
    print(" " + board[4] + " " + "|" + " " + board[5] + " " + "|" + " " + board[6] + " ")
    print(" " + " " + " " + "|" + " " + " " + " " + "|" + " " + " " + " ")
    print("------------")
    print(" " + " " + " " + "|" + " " + " " + " " + "|" + " " + " " + " ")
    print(" " + board[1] + " " + "|" + " " + board[2] + " " + "|" + " " + board[3] + " ")
    print(" " + " " + " " + "|" + " " + " " + " " + "|" + " " + " " + " ")

def player_input():
    mark = ""
    while not mark:
        mark = input("\nSelect 'X' or 'O' as your marker: ")
        if mark not in 'xXoO':
            print('\nYou must select "X" or "O" for your marker!')
            mark = ""
        else:
            return mark.upper()

def place_marker(board, marker, pos):
    board[pos] = marker

def win_check(board, mark):
    mk = set(mark)
    result = bool
    if set(board[1:4]) == mk or set(board[4:7]) == mk or set(board[7:]) == mk:
        result = True
    elif set(board[1::3]) == mk or set(board[2::3]) == mk or set(board[3::3]) == mk:
        result = True
    elif set(board[1::4]) == mk or set(board[3:9:2]) == mk:
        result = True
    else:
        result = False
    return result

import random

def choose_first():
    mark = random.randint(1,3)
    if mark == 1:
        return 'X'
    else:
        return 'O'
    
def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    result = True
    for i in board:
        if i == ' ':
            result = False
    return result

def player_choice(board):
    pos = 0
    while pos not in range(1,10):
        try:
            pos = int(input("\nEnter a position number from 1 to 9: "))
        except ValueError:
            print('\nYou must enter a number from 1 to 9!')
    available = space_check(board, pos)
    if available == True:
        return pos
    else:
        return "Not available."
    
def replay():
    result = bool
    ans = ''
    while not ans:
        try:
            ans = input("Play again? (y/n) ")
        except:
            print('\nYou must enter y for yes or n for no.')
        if ans in 'Yy':
            result = True
        elif ans in 'Nn':
            result = False
        else:
            print('\nYou must enter y for yes or n for no!')
            ans = ''
    
    return result

game_on = True
print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player_input()
    first_player = choose_first()
    if first_player == 'X':
        second_player = 'O'
        print('\nPlayer1 goes first')
    else:
        first_player = 'O'
        second_player = 'X'
        print('\nPlayer2 goes first')

    while game_on:
        # Player 1 Turn
        position = player_choice(test_board)
        while position in range(1, 10):
            place_marker(test_board, first_player, position)
            break
        else:
            print('Position not available.  Select another position from 1 to 9')
            position = player_choice(test_board)
        display_board(test_board)
        fp_win = win_check(test_board, first_player)
        if fp_win == False:
            game_on = True
        else:
            if first_player == 'X':
                print('\nPlayer 1 wins!')
            else:
                print('\nPlayer 2 wins!')
            game_on = False
            break
        if full_board_check(test_board) == True:
            print('\nBoard is full!')
            break
        
        # Player2's turn.
        position = player_choice(test_board)
        while position in range(1, 10):
            place_marker(test_board, second_player, position)
            break
        else:
            print('Position not available.  Select another position from 1 to 9')
            position = player_choice(test_board)
        display_board(test_board)
        sp_win = win_check(test_board, second_player)
        if sp_win == False:
            game_on = True
        else:
            if second_player == 'O':
                print('\nPlayer 2 wins!')
            else:
                print('\nPlayer 1 wins!')
            game_on = False
            break
        if full_board_check(test_board) == True:
                print('\nBoard is full!')
                break

    if not replay():
        break
    else:
        game_on = True