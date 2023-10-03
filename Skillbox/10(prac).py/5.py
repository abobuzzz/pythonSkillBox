n = int(input('Enter amount of numbers: '))
lag_sum, lag_num = 0, 0

for numb in range(n):
    number = int(input('Enter nature numb: '))
    sum = 0 
    mid_num = number
    while mid_num != 0:
        sum = sum + mid_num % 10
        mid_num = mid_num // 10
        if sum > lag_sum:
            lag_sum = sum
            lag_num = number 

print(f'\nEver big numb: {lag_sum}')