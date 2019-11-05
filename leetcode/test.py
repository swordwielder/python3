import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = 4
a=n
plus="+"
for i in range(n):
    for n in range(a):

        print('+',end="")
	print(n+1,end="")
    a-=1
    print()

numbers=''.join([str(i) for i in range(1,5)])


for i in range(0,n):
    print(i*'+'+numbers)
    numbers= numbers[:-1]



# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

