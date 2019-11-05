import math
cx,cy=[int(i) for i in input().split()]
r = int(input())
n = int(input())
t=0
for i in range(n):
    x,y=[int(j) for j in input().split()]
    #radius is the distance, distance formula
    if (x-cx)**2+(y-cy)**2<=r**2:
        t+=1
print(round((t/n)*100))
