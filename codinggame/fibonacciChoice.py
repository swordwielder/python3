x,y=map(int,input().split())
n=int(input())
if n==1:print(x)
elif n==2:print(y)
else:
 t=x+y
 for i in range(3,n):
  x=y
  y=t
  t=x+y
 print(t)




#recursion

fi= [int(i) for i in input().split()]
n = int(input())
def f(n): 
    if n<=len(fi): 
        return fi[n-1] 
    else: 
        t = f(n-1)+f(n-2) 
        fi.append(t) 
        return t 
print(f(n))

