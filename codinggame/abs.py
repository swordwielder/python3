p=input
a,b=map(int,p().split())
m=2000
n=0
for i in range(int(p())):
 x,y=map(int,p().split())
 d=abs(x-a)+abs(y-b)
 if d<m:m=d;n=i+1
print(n,m)
