sequence = input()
t=0
for i in sequence:
    n=ord(i)
    if i.isalpha():
        if n<97:
            n=n-64
            t+=n*2
        else:
            t+=n-96
a=str(t)
while len(a)<6:
    a+='0'
if len(a)>6:
    print(a[:6])
else:
    print(a)
    
    
    
    
import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

sequence = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

words = re.findall('[a-zA-Z]', sequence)
o=[ord(s)-97+1 if s.islower() else (ord(s.lower())-97+1)*2 for s in words if s != ' ']
print('{:<06d}'.format(sum(o)))
