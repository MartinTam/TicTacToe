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
import functionsModule
import subprocess

field = drawModule.createField()
win = 0
player1 = True
player2 = False

while win == 0:

    sign = ' '
    play = 0

    subprocess.call('clear')
    drawModule.printField(field)

    if player1 == True:
        sign = input('Player 1: ')
        play = 1
        player1 = False
        player2 = True
    elif player2 == True:
        sign = input('Player 2: ')
        play = 2
        player1 = True
        player2 = False

    if sign == 'q':
        break

    functionsModule.addToField(field, sign, play)
    play = 0

    win = functionsModule.checkForWin(field)


    if win == 1:
        subprocess.call('clear')
        drawModule.printField(field)
        print('PLAYER 1 WIN THE GAME!')
        print()
        break
    elif win == 2:
        subprocess.call('clear')
        drawModule.printField(field)
        print('PLAYER 2 WIN THE GAME!')
        print()
        break