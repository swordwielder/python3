import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
new = list(s)
for i in range(len(new)):
    if i%2==1:
        temp = new[i]
        new[i] = new[i-1]
        new[i-1]=temp
        
    
a=""
for i in new:
    a+=i

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(a)
