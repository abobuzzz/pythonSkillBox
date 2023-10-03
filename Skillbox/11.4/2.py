import math 

distance = float(input('Enter distance: '))
angle = float(input('Enter angle of rotation: '))

angle /= 57.2958
x = distance * math.cos(angle)
y = distance * math.sin(angle)

print('New coordinates: ', x, ',', y )