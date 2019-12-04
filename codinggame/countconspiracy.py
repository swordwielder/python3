n=int(input())
l=input().split()
m=max(l,key=l.count)
print(['conspiracy',m][l.count(m)>n/2])



x=int(input())
n=input().split()
c=0
b=''
for i in n:
    if n.count(i)>c:
        c=n.count(i)
        b=i
if c>len(n)/2:
    print(b)
else:
    print("conspiracy")
