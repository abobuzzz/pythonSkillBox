number = int(input('Enter first number: '))
step = int(input('Enter step: '))
summ = 0 

print('\nIP-адрес:', end=' ')
for count in range(3):
    print(number, end= ('.'))
    summ += number
    number += step
print(summ)
    