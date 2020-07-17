import math
a=int(input())
b=int(input())
s=math.floor(a**(1/2))
t=0
while s**2<=b:
 if s**2>=a:t+=1
 s+=1
print(t)
