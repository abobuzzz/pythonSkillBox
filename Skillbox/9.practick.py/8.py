word = input('Enter word: ')
unword1 = ''    
unword2 = ''
count = 0
for symbol in word:
    if symbol:
        unword1 = symbol + unword1
for symbol2 in word:
    if symbol2:
        unword2 += symbol2
if unword1 == unword2:
        print('Да, это слово палиндром!')
else:
        print('Нет, это слово не палиндром!')

