def mostBig(numb):
    count = 0
    while numb > 0:
        numb //= 10
        count += 1
    return count
def max(quant):
    max_count = 0
    max_numb = 0
    mostBig(quantity)
    if quantity < 0:
        max_count = 0
    mosty = max(quantity)
    if quantity > max_count:
        max_count = mosty
        max_numb = quantity
    return max_numb
quantity = int(input('Enter quantity numbers: '))
print('Firts work: ', max(quantity))