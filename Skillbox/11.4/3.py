import math

number = int(input('Enter number: '))

floor = math.floor(number)
print('Number floor: ', floor)

ceil = math.floor(number)
print('Number ceil: ', ceil)

module = abs(number)
print('Number module: ', module)

quadro = math.sqrt(number)
print('Number SQRT: ', quadro)

exp = math.exp(number)
print('Number exp: ', exp ** number)

log = math.log(number)
print('Natural log number: ', log)

log2 = math.log2(number)
print('Logorifm to 2: ', log2)

log10 = math.log10(number)
print('Number logo10: ', log10)

sin = math.sin(number)
cos = math.cos(number)
print('Cos: ', cos, 'Sin: ', sin)

if number % 1 == 0:
    fact = math.factorial(number)
    print('Number factorial: ',fact)
    