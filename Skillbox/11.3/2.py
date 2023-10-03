print('Enter coordinates figure')
x = float(input('Horizontally: '))
y = float(input('Verticaly: '))
print()

if x > 0.8 or x < 0:
    print("You've gone beyond the border!")
    x = float(input('Try again!: '))
elif y > 0.8 or y < 0:
    print("You've gone beyond the border!") 
    y = float(input('Try again!: '))

xSquare = int(x * 10)
ySquare = int(y * 10)

print('Figyre located at the coordinates:', xSquare, ySquare)