player1 = input("Please pick a marker 'X' or 'O' ").upper()
while not player1:
    player1 = input("Please pick a marker 'X' or 'O' ").upper()

while player1:
    if player1 == 'X' or player1 == 'O':
        break
    else:
        player1 = input("Please pick a marker 'X' or 'O' ").upper()

print(player1)