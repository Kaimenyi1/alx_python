for number in range(10):
    for digit in range(number + 1, 10):
        print("{:d}{:d}".format(number, digit), end="" )
        if not number +1>8:
            print(', ',end='')
        else:
            print(' ')
