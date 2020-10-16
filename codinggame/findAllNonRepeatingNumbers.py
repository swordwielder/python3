n=int(input())
a={}
for i in input().split():
 v=int(i)
 if v not in a:a[v]=1
 else:a[v]+=1
for k,v in a.items():
 if v==1:print(k)


