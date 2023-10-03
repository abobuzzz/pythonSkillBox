height = float(input('Enter your height: '))
weight = float(input('Enter your weight: '))

bmi =  round(weight / height ** 2, 2)
print('Your BMI:', bmi)

if bmi <= 18.5:
    print('You have small weight!')
elif bmi <= 25:
    print('You have normal weight!')
elif bmi <= 30:
    print('You have oversupply weight!')
else:
    print('You have obesity!')
