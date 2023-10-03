step = int(input('Введите число: '))
for row in range(step + 1):
    for col in range(step + 1):
        print(row + col, end= ' ')
    print()