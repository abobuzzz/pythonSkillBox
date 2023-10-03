def count_letters(text):
    numb = input('What number are we looking for?: ')
    letter = input('What letter are you locking for?: ')
    square_numb = 0
    square_letter = 0 
    for symbol in text:
        if symbol == numb:
            square_numb += 1
        elif symbol == letter:
            square_letter += 1
    print('Square number',numb ,':', square_numb)
    print('Square letter',letter, ':', square_letter)
def gpu():
    text = input('Enter text: ')
    count_letters(text)
gpu()