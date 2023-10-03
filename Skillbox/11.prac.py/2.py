import math
numbers_all = int(input('Enter quantity number: '))

for i in range(numbers_all):
    numb = float(input('Enter number: '))
    if numb > 0:
        s = math.ceil(numb)
        x = math.log(s)
        print('x =',s,'log(x) =',x)
    elif numb < 0:
        y = math.floor(numb) 
        e = math.exp(y)
        print('x =',e,'exp(x) =',y)