n = int(input('Enter number: '))
def isPrime():
    if n % 1 == 0 and n / n == 0:
        print('Number prime!')
    else:
        print('Number not prime!')
isPrime()
