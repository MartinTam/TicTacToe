'''
# Coordinates of tic and tac
field[4][17] = 'O'
field[4][25] = 'X'
field[4][33] = 'O'

field[7][17] = 'O'
field[7][25] = 'X'
field[7][33] = 'O'

field[10][17] = 'O'
field[10][25] = 'X'
field[10][33] = 'O'

'''

import drawModule

field = drawModule.createField()
drawModule.printField(field)
