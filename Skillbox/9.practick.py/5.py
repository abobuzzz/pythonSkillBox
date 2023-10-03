text = input('Введите ваш текст: ')
maxi = 0 
counter = 0
for letter in text:
    if letter == ' ':
        counter = 0
    else: 
        counter += 1
        if maxi < counter:
            maxi = counter
print('Самое длинное слово, букв:', maxi)