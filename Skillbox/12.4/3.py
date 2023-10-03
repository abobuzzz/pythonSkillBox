import math
def first(x , y):
    print('Distance from you to coordinates y: ', math.sqrt((x **2) + (y ** 2)))      

def second(x1, y1, x2, y2):
    print('Distance from two points: ', abs((x1 - x2) ** 2 + (y1 - y2) ** 2))
    
one_or_two = int(input('Enter number 1 or 2; 1 - distance from yourself to a point; 2 - distance between two arbitrary points: '))
if one_or_two == 1:
    x = float(input('Enter x coordinates: '))
    y = float(input('Enter y coordinates: '))
    first(x, y)
elif one_or_two == 2:
    x1 = float(input('Enter x1 coordinates: '))
    y1 = float(input('Enter y1 coordinates: '))
    x2 = float(input('Enter x2 coordinates: '))
    y2 = float(input('Enter y2 coordinates: '))
    second(x1, y1, x2, y2)
else:
    print('Error!')
    