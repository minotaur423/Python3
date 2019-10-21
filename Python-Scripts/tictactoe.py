#from IPython.display import clear_output

def display_board(board):
    #clear_output()
    result = ''
    tbl = { 'line1':'   |   |   \n', \
            'area7':'   ', 'line2-1':'|', 'area8':'   ', 'line2-2':'|', 'area9':'   ', 'line2-3':'\n', \
            'line3':'   |   |   \n', 'line4':'-----------\n', \
            'line5':'   |   |   \n', \
            'area4':'   ', 'line6-1':'|', 'area5':'   ', 'line6-2':'|', 'area6':'   ', 'line6-3':'\n', \
            'line7':'   |   |   \n', 'line8':'-----------\n', \
            'line9':'   |   |   \n', \
            'area1':'   ', 'line10-1':'|', 'area2':'   ', 'line10-2':'|', 'area3':'   ', 'line10-3':'\n', \
            'line11':'   |   |   \n' }

    for num in range(1,10):
        tbl['area' + str(num)] = ' ' + board[num] + ' '

    for i,j in tbl.items():
        result += tbl[i]
    
    return result


test_board = ['#','X','O','X','O','X','O','X','O','X']
print(display_board(test_board))