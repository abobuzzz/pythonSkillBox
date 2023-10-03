def reverse(number):
    b = ''
    c = 0
    for i in number:
        c += 1 
        if b == '0' and (c == 1, c == 2, c == 3):
            b = '' + b
        else:
            b = i + b
    print('Numb reverse:', b)
def end(number):
    print('Programm end!')
def start():
    number = input('Enter number: ')
    if number > '0' or number < '0':
        reverse(number)
        start()
    elif number == 0:
        end(number)
    print('Programm end!')
start()

