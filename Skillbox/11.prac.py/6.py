import math 
print('Введите местоположение коня: ')
a = float(input())
b = float(input())
print('Введите местополодение точки на доске: ')
x = float(input())
y = float(input())
asq = a * 10
bsq = b * 10
xsq = x * 10
ysq = y * 10
print('Конь в клетке:','(',math.floor(asq), math.floor(bsq),')', end='. ')
print('Точка в клетке: ','(', math.floor(xsq), math.floor(ysq),')')
if asq + 2 or - 2 == xsq and bsq + 1 or - 1 == ysq:
    print('Да, конь может ходить в эту точку!')
else:
    print('Нет, конь не может ходить в эту точку!')