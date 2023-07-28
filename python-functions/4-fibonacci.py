def fibonacci_sequence(n) :
    if n <= 0 :
        return[]
    elif n==1:
       return[0]
    else:
        fib_sequence=[0 ,1,1,2,3,5]
        while len(fib_sequence)<n :
            next_num = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_num)
        return fib_sequence

        
print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))
