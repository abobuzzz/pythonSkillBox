import math
radius = float(input('Enter radius random planet: '))
earth = 1.08321 * 10 ** 12

V = 4/3 * math.pi * radius ** 3

if V < earth:
    print('The volume is less in: ', round(earth / V , 3))
elif V > earth:
    print('Volume is greater in: ', round(V / earth, 3))
    