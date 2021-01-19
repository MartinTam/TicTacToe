
def addToField(field, sign, play):

    putIn = ' '

    if play == 1:
        putIn = 'O'
    elif play == 2:
        putIn = 'X'

    # First row
    if sign == 'a1' or sign == 'A1':
        field[4][17] = putIn
    elif sign == 'a2' or sign == 'A2':
        field[4][25] = putIn
    elif sign == 'a3' or sign == 'A3':
        field[4][33] = putIn
    
    # Second row
    elif sign == 'b1' or sign == 'B1':
        field[7][17] = putIn
    elif sign == 'b2' or sign == 'B2':
        field[7][25] = putIn
    elif sign == 'b3' or sign == 'B3':
        field[7][33] = putIn

    # Third row
    elif sign == 'c1' or sign == 'C1':
        field[10][17] = putIn
    elif sign == 'c2' or sign == 'C2':
        field[10][25] = putIn
    elif sign == 'c3' or sign == 'C3':
        field[10][33] = putIn
    
    

# Checking if either player 1 or 2 win
def checkForWin(field):

    win = 0

    # Horizontal Rows
    if ( field[4][17] == field[4][25] and field[4][25] == field[4][33] ) and ( field[4][17] == 'X' or field[4][17] == 'O' ):
        if field[4][17] == 'O':
            win = 1
        elif field[4][17] == 'X':
            win = 2
    
    elif ( field[7][17] == field[7][25] and field[7][25] == field[7][33] ) and ( field[7][17] == 'X' or field[7][17] == 'O' ):
        if field[7][17] == 'O':
            win = 1
        elif field[7][17] == 'X':
            win = 2
    
    elif ( field[10][17] == field[10][25] and field[10][25] == field[10][33] ) and ( field[10][17] == 'X' or field[10][17] == 'O' ):
        if field[10][17] == 'O':
            win = 1
        elif field[10][17] == 'X':
            win = 2
    
    # Vertical Cols
    elif ( field[4][17] == field[7][17] and field[7][17] == field[10][17] ) and ( field[4][17] == 'X' or field[4][17] == 'O' ):
        if field[4][17] == 'O':
            win = 1
        elif field[4][17] == 'X':
            win = 2
    
    elif ( field[4][25] == field[7][25] and field[7][25] == field[10][25] ) and ( field[4][25] == 'X' or field[4][25] == 'O' ):
        if field[4][25] == 'O':
            win = 1
        elif field[4][25] == 'X':
            win = 2
    
    elif ( field[4][33] == field[7][33] and field[7][33] == field[10][33] ) and ( field[4][33] == 'X' or field[4][33] == 'O' ):
        if field[4][33] == 'O':
            win = 1
        elif field[4][33] == 'X':
            win = 2

    # Diagonals

    elif ( field[4][17] == field[7][25] and field[7][25] == field[10][33] ) and ( field[4][17] == 'X' or field[4][17] == 'O' ):
        if field[4][17] == 'O':
            win = 1
        elif field[4][17] == 'X':
            win = 2
        
    elif ( field[4][33] == field[7][25] and field[7][25] == field[10][17] ) and ( field[4][33] == 'X' or field[4][33] == 'O' ):
        if field[4][33] == 'O':
            win = 1
        elif field[4][33] == 'X':
            win = 2
    
    return win