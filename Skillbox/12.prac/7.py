import random

def scissor(kmn):
    number = random.randrange(1, 3)
    if kmn == 'Ножницы' and number == 1:
        print('Losing! But stone!')
        rock_paper_scissors()
    elif kmn == 'Ножницы' and number == 2:
        print('Winning! But paper!')
        rock_paper_scissors()
    elif kmn == 'Ножницы' and number == 3:
        print('Draw! But scirssor!')

def paper(kmn):
    number = random.randrange(1, 3)
    if kmn == 'Бумага' and number == 1:
        print('Winnig! But stone!')
        print('')
        rock_paper_scissors()
    elif kmn == 'Бумага' and number == 2:
        print('Draw! But paper!')
        rock_paper_scissors()
    elif kmn == 'Бумага' and number == 3:
        print('Losing! But scirssor!')

def rock(kmn):
    number = random.randrange(1, 3)
    if kmn == 'Камень' and number == 1:
        print('Draw! But stone!')
        rock_paper_scissors()
    elif kmn == 'Камень' and number == 2:
        print('Losing! But paper!')
        rock_paper_scissors()
    elif kmn == 'Камень' and number == 3:
        print('Winnig! But scirssor!')
        rock_paper_scissors()

def rock_paper_scissors():
    kmn = input('Enter rock paper or scissors: ')
    rock(kmn)
    paper(kmn)
    scissor(kmn)  

def guess_the_number():
    random_numb = random.randrange(1, 100)
    print('Guess a number from 1 to 100')
    number = int(input('Enter your numb: '))
    if number == random_numb:
        print('You guessed it! Well done!')
    elif number != random_numb:
        print('No! Not guessed it')
    
    while number != random_numb:
        number = int(input('Enter your numb: '))
        if number == random_numb:
            print('You guessed it! Well done!')
            mainMenu()
            break
        elif number != random_numb:
            print('No! Not guessed it')

def mainMenu():
    print('1 - rock paper scissors game; 2 - guess the number')
    numb = int(input('Enter what game you want to play: '))
    if numb == 1:
        rock_paper_scissors()
    elif numb == 2:
        guess_the_number()
    else:
        print('Error!')
mainMenu()