text = input('Введите ваш текст: ')
first = input('Введите вашу первую букву: ') 
second = input('Введите вашу вторую букву: ')
first_summ = 0
second_summ = 0
for i in text:
    if i == first:
        first_summ += 1
    if i == second:
        second_summ += 1
print('Всего первых букв',first_summ,'Всего вторых букв', second_summ)