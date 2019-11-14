import sys
import math

n = int(input())
if n<2:
    print("NONE")
elif n%2==0:
    print(2)
else:
    i = 2
    while i <= n:
        if n % i==0:
            break
        else:
            i+=1
    print(i)
            
