word = input('Введите зашифрованное слово: ')
unword1 = ''    
unword2 = ''
count = 0
for symbol in word:
    count += 1
    if count % 2 == 0:
        unword2 = symbol + unword2
    elif count % 2 == 1:
        unword1 += symbol
print(unword1 + unword2)