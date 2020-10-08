

n = int(input())
m = int(input())
a=[]
for i in input().split():
    p = int(i)
    a.append(p)
for i in input().split():
    x = int(i)
    f=True
    for j in a:
        if x%j!=0:
            f=False
    if f:
        print('T',end='')
    else:
        print('F',end='')



#sol 2
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
m = int(input())
p=list(map(int,input().split()))
x = list(map(int,input().split()))

for i in x:
    if any([i%P for P in p]):
        print ('F',end='')
    else:
        print ('T',end='')

