import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
L = []
for i in input().split():
    L += [int(i)]
direction, pos = input().split()
pos = int(pos)
pos = pos%len(L)
if (direction == "Left"):
    L = L[pos:] + L[:pos]
else:
    L = L[len(L) - pos:] + L[:len(L) - pos]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(*L)



import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a = []
for i in input().split():
    temp = int(i)
    a.append(temp)

direction, pos = input().split()
pos = int(pos)

for i in range(pos):
    if direction == "Left":
        t = a [0]
        for j in range(0, len(a)-1):
            a[j] = a[j+1]
        a[len(a) - 1] = t
    else:
        t = a [len(a) - 1]
        for j in range(len(a)-1,0,-1):
            a[j] = a[j-1]
        a[0] = t

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

s = [str(v) for v in a]
print(' '.join(s))



#broken

from collections import deque


n = int(input())
a=[]
items=None
for i in input().split():
    a.append(i)
    items = deque(a)
direction, pos = input().split()
pos = int(pos)
if direction=='left':
    items.rotate(pos)
else:
    items.rotate(-pos)
b=list(items)
print(' '.join(b))

