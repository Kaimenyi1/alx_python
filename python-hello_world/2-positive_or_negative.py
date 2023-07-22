import random
number = random.randint(-10, 10)
if number> 0:
    print(format(number),"is positive \n")
elif number == 0:
    print(format(number),"is_zero \n")
else:
    print(format(number),"is negative \n")