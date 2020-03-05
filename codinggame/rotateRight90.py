import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
a=[[*map(int, input().split())] for i in range(l)]


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

b=np.rot90(np.array(a),3)
for i in b:
    print(*i)




l = int(input())
h = int(input())

t=[]
for i in range(l):
    hh=[]
    for j in input().split():
        num = int(j)
        hh.append(num)
    t.append(hh)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

for j in range(h):
    g=[]
    for i in reversed(range(l)):
        g+=[t[i][j]]
    print(*g)




import numpy as np
l=int(input())
h =int(input())
a=[]
b=[]
for i in range(l):
    for j in input().split():
        num = int(j)
        a.append(num)
    b.append(a)
    a=[]
c=np.rot90(b,3)
d=""
for i in c:
    for j in i:
        d+=str(j)+' '
    print(d[:-1])
    d=''

