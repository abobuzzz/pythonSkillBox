def min(number):
    for i in range(1, number + 1):
        if number > 0:
            print(i)
            break
        elif number < 0:
            print(-1)
            break
def max(number):
    max = 0
    for i in range(1, number + 1):
        max += i
    print('max: ', max)
def summ(number):
    sum_numb = 0
    for i in range(1, number + 1):
        sum_numb += i 
    print('Sum:',sum_numb)
def start():
    print('1 - display the sum figure; 2 - display max figure; 3 - display min figure')
    action = int(input('Enter action: '))
    number = int(input('Enter number: '))
    if action == 1:
        summ(number)
        start()
    elif action == 2:
        max(number)
        start()
    elif action == 3:
        min(number)
start()



