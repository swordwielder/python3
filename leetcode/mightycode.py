import sys
import math

number = int(input())
overten=number
norm=1
less=0
numbers=''.join([str(i) for i in range(1,number+1)])

for i in range(0,number):
    if norm>0:
        print(numbers)
    else:
        print(numbers[::-1])
    if overten <10:
        numbers=numbers[:-1]
        overten-=1
    else:
        numbers=numbers[:-2]
        overten-=1
    norm*=-1
