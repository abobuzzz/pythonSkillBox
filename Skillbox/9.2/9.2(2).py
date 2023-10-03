dueses = 0
for chaild in range(5):
    question = input('Кто написал произведение Евгений Онегин? ')
    if (question == 'Пушкин') or (question == 'пушкин'):
        print('Верно!')
        break
    print('Садись, два!')
    dueses += 1 
print('За сегодня двоек:',dueses)
