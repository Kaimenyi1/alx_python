import random
number = random.randint(-10000, 10000)
Last_digit=int(str(number)[-1])
if Last_digit> 5:
    print(f"Last digit of {number} is {Last_digit} and is greater than 5 \n")
elif Last_digit==0:
   print(f"Last digit of {number} is {Last_digit} and is o \n")
else:
    print(f"Last digit of {number} is {Last_digit} and is less than 6 and not 0 \n")
   