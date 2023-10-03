n = int(input('Введите число: '))
s = 0
for row in range(1, n + 1):
    for col in range(1, n + 1):
        if col <= row:
            print(row, end=' ')
        elif col == 5:
            print()
        else:
            print(' ', end=' ')