import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

g = int(input())
s = int(input())
b = int(input())


while b >=100:
    b-=100
    s+=1
while s >=100:
    s-=100
    g+=1

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(g,"G ",s,"S ",b,"B",sep="")
