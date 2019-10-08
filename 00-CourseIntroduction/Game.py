import random

game = [[" ", " ", " "],
	[" ", " ", " "],
	[" ", " ", " "]]
turn = 0
print("")
print("  " + game[0][0] +" | " + game[0][1] +" | " + game[0][2] +"  ")
print(" ---+---+---")
print("  " + game[1][0] +" | " + game[1][1] +" | " + game[1][2] +"  ")
print(" ---+---+---")
print("  " + game[2][0] +" | " + game[2][1] +" | " + game[2][2] +"  ")
print(" ")
while 1:
#VERTICALLY
    if game[0][0] == game[1][0] == game [2][0]:
        if game[0][0] == "X":
            print('player 1 wins')
            break
        elif game[0][0] == "O":
            print('player 2 wins')
            break

    elif game[0][1] == game[1][1] == game [2][1]:
        if game[0][1] == "X":
            print('player 1 wins')
            break
        elif game[0][1] == "O":
            print('player 2 wins')
            break

    elif game[0][2] == game[1][2] == game [2][2]:
        if game[0][2] == "X":
            print('player 1 wins')
            break
        elif game[0][2] == "O":
            print('player 2 wins')
            break
#DIAGONALLY
    elif game[0][0] == game[1][1] == game [2][2]:
        if game[0][0] == "X":
            print('player 1 wins')
            break
        elif game[0][0] == "O":
            print('player 2 wins')
            break

    elif game[0][2] == game[1][1] == game [2][0]:
        if game[0][2] == "X":
            print('player 1 wins')
            break
        elif game[0][2] == "O":
            print('player 2 wins')
            break
#HORIZONTALLY
    elif game[0][0] == game[0][1] == game [0][2]:
        if game[0][0] == "X":
            print('player 1 wins')
            break
        elif game[0][0] == "O":
            print('player 2 wins')
            break

    elif game[1][0] == game[1][1] == game [1][2]:
        if game[1][0] == "X":
            print('player 1 wins')
            break
        elif game[1][0] == "O":
            print('player 2 wins')
            break

    elif game[2][0] == game[2][1] == game [2][2]:
        if game[2][0] == "X":
            print('player 1 wins')
            break
        elif game[2][0] == "O":
            print('player 2 wins')
            break
    while 2:
        while 2.1:
            column = int(input("What column do you want to place the 'X'?: "))
            if column in range(1,4):
                break
            else:
                print("There are only 3 columns, choose: 1, 2 or 3")
        while 2.2:
            row    = int(input("What row do you want to place the 'X'?: "))
            if row in range(1,4):
                break
            else:
                print("There are only 3 columns, choose: 1, 2 or 3")            
        if column < 4 and column > 0 and row < 4 and row > 0:
            if game[column-1][row-1] != "O" and game[column-1][row-1] != "X":
                game[column-1][row-1] = "X"
                print("")
                print("  " + game[0][0] +" | " + game[0][1] +" | " + game[0][2] +"  ")
                print(" ---+---+---")
                print("  " + game[1][0] +" | " + game[1][1] +" | " + game[1][2] +"  ")
                print(" ---+---+---")
                print("  " + game[2][0] +" | " + game[2][1] +" | " + game[2][2] +"  ")
                print(" ")
                turn += 1
                break
            else:
                print("That spot is taken")
#VERTICALLY
    if game[0][0] == game[1][0] == game [2][0]:
        if game[0][0] == "X":
            print('player 1 wins')
            break
        elif game[0][0] == "O":
            print('player 2 wins')
            break

    elif game[0][1] == game[1][1] == game [2][1]:
        if game[0][1] == "X":
            print('player 1 wins')
            break
        elif game[0][1] == "O":
            print('player 2 wins')
            break

    elif game[0][2] == game[1][2] == game [2][2]:
        if game[0][2] == "X":
            print('player 1 wins')
            break
        elif game[0][2] == "O":
            print('player 2 wins')
            break
#DIAGONALLY
    elif game[0][0] == game[1][1] == game [2][2]:
        if game[0][0] == "X":
            print('player 1 wins')
            break
        elif game[0][0] == "O":
            print('player 2 wins')
            break

    elif game[0][2] == game[1][1] == game [2][0]:
        if game[0][2] == "X":
            print('player 1 wins')
            break
        elif game[0][2] == "O":
            print('player 2 wins')
            break
#HORIZONTALLY
    elif game[0][0] == game[0][1] == game [0][2]:
        if game[0][0] == "X":
            print('player 1 wins')
            break
        elif game[0][0] == "O":
            print('player 2 wins')
            break

    elif game[1][0] == game[1][1] == game [1][2]:
        if game[1][0] == "X":
            print('player 1 wins')
            break
        elif game[1][0] == "O":
            print('player 2 wins')
            break

    elif game[2][0] == game[2][1] == game [2][2]:
        if game[2][0] == "X":
            print('player 1 wins')
            break
        elif game[2][0] == "O":
            print('player 2 wins')
            break
    if turn == 9:
        print("It's a tie")
        break
    while 3:
        column_1 = random.randint(0,2)
        row_1    = random.randint(0,2)
        if game[column_1][row_1] != "O" and game[column_1][row_1] != "X":            
            game[column_1][row_1] = "O"
            print("")
            print("  " + game[0][0] +" | " + game[0][1] +" | " + game[0][2] +"  ")
            print(" ---+---+---")
            print("  " + game[1][0] +" | " + game[1][1] +" | " + game[1][2] +"  ")
            print(" ---+---+---")
            print("  " + game[2][0] +" | " + game[2][1] +" | " + game[2][2] +"  ")
            print(" ")
            turn += 1
            break
        else:
            print("That spot is taken")
