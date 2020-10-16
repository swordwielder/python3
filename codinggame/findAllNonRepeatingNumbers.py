n=int(input())
a={}
for i in input().split():
 v=int(i)
 if v not in a:a[v]=1
 else:a[v]+=1
for k,v in a.items():
 if v==1:print(k)


#sol2

n=int(input())
t=[i for i in input().split()]
for i in t:
    if t.count(i)==1:print(i)


#sol3
i=input
n=i()
s=i().split()
print([v for v in s if s.count(v) ==1][0])

