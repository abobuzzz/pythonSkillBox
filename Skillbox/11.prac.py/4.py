import math
x = float(input('Enter number x: '))
y = float(x, -1)
print(y)
stars = 1
for i in range(5):
    print(' ' * (5 - i - 1), end='')
    print('*' * stars)
    stars += 2