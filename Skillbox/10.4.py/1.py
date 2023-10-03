people_num = int(input('Введите количество людей в очереди: '))
for hour in range(people_num + 1):
    print('Идет час:',hour)
    for numb in range(hour, people_num):
        print('Номер в очереди: ',numb)
    print()