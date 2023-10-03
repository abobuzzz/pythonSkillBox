n = int(input('Enter number: '))
negro = ''
for number in range(n + 1):
    if (number % 10 == 0) or (number == 0):
        print(number, end=('-=-'))

        
