pirat = input('Введите текст: ')
summ = 0
for i in pirat:
    summ += 1
    if i ==('*'):
        print('Звездочка найдена! Она стоит на позиции',summ)