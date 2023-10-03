print('Enter coordinates figure')
x = float(input('Horizontally: '))
y = float(input('Verticaly: '))
print()

darkX = round(x, 1)
darkY = round(y, 1)

if x <= 0.8 or x >= 0 and y >= 0 or y <= 0.8:
    SqaureX = int(x * 10)
    SquareY = int(y * 10)
    dark_park = round(darkX- x, 3)
    dark_age = round(darkY - y, 3)
    
else:
    print('You are back to the border!')
    
print('Figyre located at the coordinates:', SqaureX, SquareY )
print('Needs to be corrected to: ', dark_park, dark_age)