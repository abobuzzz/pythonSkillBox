first_coordi = 8
second_coordi = 10

while True:
    print('\n[Программа]: Марсоход находится на позиции',first_coordi, second_coordi, 'введите команду:')
    programm = input('[Оператор]: ')
    if programm == 'W' and first_coordi <= 15:
        first_coordi += 1
        if first_coordi == 15:
            print('Прямо больше нельзя!')
    elif programm == 'S' and first_coordi >= 0:
        first_coordi -= 1
        if first_coordi == 0:
            print('Назад больше нельзя!')
    elif programm == 'A' and second_coordi >= 0:
        second_coordi -= 1
        if second_coordi == 0:
            print('Влево больше нальзя!')
    elif programm == 'D' and second_coordi <= 20:
        second_coordi += 1
        if second_coordi == 20:
            print('Вправо больше нельзя!')