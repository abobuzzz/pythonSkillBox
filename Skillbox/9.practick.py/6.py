first_stall = 2
for i in range(9):
    a_or_b = input('Введите значение a/b: ')
    print(first_stall)
    if a_or_b == 'a':
        first_stall += 2
    else:
        first_stall += 4    