for row in range(30):
    for col in range(20):
        if row > 0 and row < 30:
            print('-',end='')
        elif col:
            print('|')            