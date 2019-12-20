import sys
import math

t, h, w = input().split()
t = float(t)
h = int(h)
w = int(w)
i=0
while t<h:
    t*=2
    i+=1
print(i)
print(2**i*w)
