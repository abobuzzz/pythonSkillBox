text = input('Введите текст: ')
first_letter = input('Введите первую букву: ')
second_letter = input('Введите вторую букву: ')
first_letter_sum = 0
second_letter_sum = 0

for symbol in text:
    if symbol == first_letter:
        first_letter_sum += 1 
    if symbol == second_letter:
        second_letter_sum += 1

print('В тексте букв', first_letter,'всего: ',first_letter_sum )
print('В тексте букв', second_letter,'всего: ', second_letter_sum)
   