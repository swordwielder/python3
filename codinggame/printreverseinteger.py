import sys
import math


n = int(input())
a=[]
for i in input().split():
    a.append(int(i))
a.sort(reverse=True)
if a[0]==0:
    print(0)
else:
    for i in a:
        print(i,end='')





n = int(input())
s=''.join(sorted(input().split())[::-1])
print(int(s))

