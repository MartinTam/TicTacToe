
def createField():

    field = []

    # Create the Field
    for row in range(13):
        temp = []

        for col in range(39):
            temp.append(' ')
        field.append(temp)

    # Draw horizontal lines of Field
    for x in range(2,13,3):
        for y in range(14,37):
            field[x][y] = '_'

    # Draw vertical lines of Field 
    for x in range(3, 12):
        for y in range(13,39,8):
            field[x][y] = '|'
    
    # Write coordinates of the Field
    field[1][17] = 1
    field[1][25] = 2
    field[1][33] = 3

    field[4][8] = 'a'
    field[7][8] = 'b'
    field[10][8] = 'c'

    return field


def printField(field):

    # Print the Field
    for rows in range(13):
        for cols in range(39):
            print(field[rows][cols], end='')
        print()
    print()
    print('-------------------------------------------------------')
    print('Help: q - Quit the game')
    print()