step = int(input('Введите значение: '))
for row in range(1, step + 1):
    for col in range(1, step + 1):
        if row % 2 == 0:
            print(row, end=' ')
        else:
            print(col, end=' ')
    print()