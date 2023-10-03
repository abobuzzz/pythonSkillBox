def summa_n(N):
    if N > 0:
        all_numb = 0
        for i in range(1, N + 1):
            all_numb += i
        print('Sum all number from 1 to', N, '=', all_numb)
    else:
        print('Error!')
N = int(input('Enter number: '))
summa_n(N)
