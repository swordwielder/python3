import sys
import math

n = int(input())
total=0
for i in input().split():
    number = int(i)
    if (number <10):
       total +=number 
    else:
        a=str(number)
        for i in a:
            total+=int(i)
    
print(total)
