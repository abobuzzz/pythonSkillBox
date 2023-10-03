size = int(input('Введите размер таблица: '))
count = 0
for row in range(1, size + 1):
    for cro in range(1, size + 1):
        if row % 2 == 0:
            print(row, end=' ')
        else:
            print(cro, end=' ')
    print()