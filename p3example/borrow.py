import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

mmm, aaa, nnn = [int(i) for i in input().split()]


#print (nnn)
money=0
for i in range(1,nnn+1):
    money=money+(i*mmm)

if (money < aaa):
    print (0)
else:
    print(money-aaa)
