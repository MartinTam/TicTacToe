
for first in range(26):
    if first==0:
        print(' ', end='')
    print('_', end='')

print()

for row in range(3):
    for col in range(0,28):
        if col == 0 or col%9==0:
            print('|', end='')
        elif row==2:
            print('_', end='')
        else:
            print(' ', end='')
    print()

for row in range(3):
    for col in range(0,28):
        if col == 0 or col%9==0:
            print('|', end='')
        elif row==2:
            print('_', end='')
        else:
            print(' ', end='')
    print()

for row in range(3):
    for col in range(0,28):
        if col == 0 or col%9==0:
            print('|', end='')
        elif row==2:
            print('_', end='')
        else:
            print(' ', end='')
    print()

print()

