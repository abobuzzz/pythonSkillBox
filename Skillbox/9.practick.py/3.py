Rows = int(input('Введите количество рядов: '))
cheer = int(input('Введите количество сидений в ряду: '))
metrs = int(input('Введите количество метров между рядами: '))
print()

for i in range(0, Rows):
    print(cheer * '=', metrs * '*', cheer * '=')
    

