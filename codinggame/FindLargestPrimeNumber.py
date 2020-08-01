#method 1
I=input
I([m for m in sorted(int(I())for _ in'*'*int(I()))[::-1]if sum(1 for j in range(2,m)if m%j==0)<1][0])


#method 2
import math,itertools
m=[]
for i in range(int(input())):m+=[int(input())]
print(max([n for n in m if n>1 and all(n%i for i in itertools.islice(itertools.count(2),int(math.sqrt(n)-1)))]))

#method 3
def a(n):
    for i in range(2,1+int(n**1/2)):
        if n%i==0:return 0
    return 1
b,n=[],int(input())
for i in range(n):
    m=int(input())
    if a(m): b.append(m)
print(sorted(b)[-1])

#method 4
def isPrime(n): 
 if (n<=3):return True
 if (n%2==0 or n%3==0):return False
 i=5
 while(i*i<=n): 
  if (n%i==0 or n%(i+2)==0):return False
  i=i+6
 return True
n=int(input())
l=0
for i in range(n):
 m=int(input())
 if isPrime(m) and m>l:l=m
print(l)
