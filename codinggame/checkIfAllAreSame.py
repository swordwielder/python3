n=int(input())
c=input()
for i in range(n):
 x=input()
 f=True
 for j in range(len(x)):
  if x[j]==c[j]:
   print('Invalid')
   f=False
   break
 if f==True:print('Valid')
 


#sol 2

z=input
n=int(z())
c=z()
for i in range(n):
 for x,y in zip(z(),c):
  if x==y:print('Invalid');break
 else:print('Valid')
 
 
