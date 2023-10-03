alll = 0
prog = 0
def alllnumb(a, b , alll , prog):
    for i in range(a, b + 1):
        alll += i
        prog += 1
    print('Average:', alll / prog)
    if b < a:
        print('Error!')
a = int(input('Enter a number: '))
b = int(input('Enter b number: '))
alllnumb(a, b, alll, prog)
