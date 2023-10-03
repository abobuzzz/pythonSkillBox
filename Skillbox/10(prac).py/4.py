counter, pack = 0, 0
n = True
print('Последовательность вводимых чисел закончите вводом 0.')

while n:
  diap = int(input('\nВведите число: '))
  counter = 0
  if diap == 0:
    n = False
  if diap == 2:
    pack += 1
  if diap % 2 != 0:
    for i in range(1, diap + 1):
      if diap % i == 0:
        counter += 1
    if counter < 3:
      pack += 1

print('\nКоличество простых чисел \nв заданной последовательности:', pack)