import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a=0
b=0

res = [int(x) for x in str(n)]
#print(len(res))
for i in range(0,len(res)):
    #print(i)
    if i%2 ==0:
        a+=res[i]
    if i%2 ==1:
        b+=res[i]

#print(a)
#print(b)
print(a-b)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
