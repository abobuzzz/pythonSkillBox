text = int(input('Введите размер таблицы: '))

for symbol in range(text):
    for col in range(text):
        buf_col = (text-1)
        if buf_col > col:
            print(0,end=' ')
        elif  buf_col < symbol:
            print(2,end=' ')
        elif symbol == buf_col:
            print(1,end=' ')
    print()