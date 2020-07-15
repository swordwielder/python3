import math
r=1
n=int(input())
for i in range(n-1):r=[r,i][math.gcd(n,i)==1]
print(r)

# second solution
n=int(input())
for x in range(n-2,1,-1):
 for c in range(2,n): 
  if not(x%c or n%c):break
 else:
  print(x)
  break

#third solution
def l(a,b):
 while b!=0:
  a,b=b,a%b
 return a
s=0
n=int(input())
for i in range (n,0,-1):
 if l(i,n)==1:
  if s==0:
   s=1
  else:
   print(i)
   exit()
