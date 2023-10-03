def possitive():
    print('Number possitive!')
def negative():
    print('Number negative')

def test():
    a = int(input('Enter number: '))
    if a > 0:
        possitive()
    elif a < 0:
        negative()

test()