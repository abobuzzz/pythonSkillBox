call = int(input('Введите количество чисел: '))
max = 0
count = 0
for numb in range(call):
    print('Введите',numb,'количество числе: ',end='')
    n = int(input())
    if n >= 9999:
        max = max + n
        count += 1
print('Числе в которых количество цифр >5:',count,'Их общая сумма: ',max)