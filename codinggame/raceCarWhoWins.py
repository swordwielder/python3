n,m=map(int,input().split())
w=0
a=float('inf')
for i in range(n):
 s,t=map(int,input().split())
 n=int((m-t)/s)
 if a>n:
  a=n
  w=i
print(w)
