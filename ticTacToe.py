
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
    subprocess.call('./header.sh')
    drawModule.printField(field)

    if player1 == True:
        sign = input('Player 1: ')

        if functionsModule.wrongInput(sign) == 1:
            
            while functionsModule.wrongInput(sign) == 1:
                subprocess.call('clear')
                subprocess.call('./header.sh')
                drawModule.printField(field)
                print(' !!! WRONG COORDINATE, PLEASE TRY AGAIN !!!')
                print()
                sign = input('Player 1: ')
            
        play = 1
        player1 = False
        player2 = True
    
    elif player2 == True:
        sign = input('Player 2: ')

        if functionsModule.wrongInput(sign) == 1:
            
            while functionsModule.wrongInput(sign) == 1:
                subprocess.call('clear')
                subprocess.call('./header.sh')
                drawModule.printField(field)
                print(' !!! WRONG COORDINATE, PLEASE TRY AGAIN !!!')
                print()
                sign = input('Player 2: ')
                
        play = 2
        player1 = True
        player2 = False

    if sign == 'q':
        print()
        break

    functionsModule.addToField(field, sign, play)
    play = 0

    win = functionsModule.checkForWin(field)


    if win == 1:
        subprocess.call('clear')
        subprocess.call('./header.sh')
        drawModule.printField(field)
        print('PLAYER 1 WIN THE GAME!')
        print()
        break
    elif win == 2:
        subprocess.call('clear')
        subprocess.call('./header.sh')
        drawModule.printField(field)
        print('PLAYER 2 WIN THE GAME!')
        print()
        break