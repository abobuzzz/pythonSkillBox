import math

a = float(input('Enter side a: '))
b = float(input('Enter side b: '))
c = float(input('Enter side c: '))

p = (a + b + c) / 2

S = math.sqrt((p * (p - a) * (p - b) * (p - c)))

print('Area of the triangle such: ', S)
