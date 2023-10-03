a = int(input('Enter frame width: '))
b = int(input('Enter frame hieght: '))

for row in range(a + 1):
    for col in range(b + 1):
        if col == 0 or col == b:
            print('|', end=' ')
        elif row == 0 or row == a:
            print('-', end=' ')
        else:
            print(' ', end=' ')
    print()