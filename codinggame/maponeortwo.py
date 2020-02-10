f=lambda:map(int,input().split())
a,x=f()
b,y=f()
k=0
while(a>0)*b>0:b-=x;a-=y;k+=1
print(2-(b<1),k)



import math
a,b=map(int,input().split())
c,d=map(int,input().split())
if d==0 or a/d>c/b:print(1,math.ceil(c/b))
else:print(2,math.ceil(a/d))
