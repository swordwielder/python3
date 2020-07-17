n=int(input())
if n==1:print(0)
else:
  x=0
  y=t=1
  a=[]
  for i in range(n):
   a.append(str(x))
   x=y
   y=t
   t=x+y
  print(' '.join(a)) 
  
  
  
  
#fibonacci second

i,z=0,5**0.5
t,p,x=(1+z)/2,(1-z)/2,[]
exec('x.append(int((t**i-p**i)/z));i+=1;'*int(input()))
print(*x)
