#prime number discrimination(use sqrt)
import math

print("you must write number(number is natural number)")
n = int(input())

if (n == 1):
    print("your %d is not a prime number" %n)
else:    
    for i in range(2,int(math.sqrt(n)+1)):
        if  n % i == 0:
            print("not prime number")
            break
    else:
        print("prime number")
