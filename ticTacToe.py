
def firstRow():
    for first in range(36):
        if first < 9:
            print(' ', end='')

        if first==9:
            print(' ', end='')
        if first > 9:
            print('_', end='')

    print()

def otherRow():

    for row in range(3):
        for col in range(37):
            if col >= 9 and col%9==0:
                print('|', end='')
            elif col>= 9 and row==2:
                print('_', end='')
            else:
                print(' ', end='')
        print()

firstRow()
for i in range(3):
    otherRow()
print()    


