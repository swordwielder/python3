n,r=[int(i) for i in input().split()]
t=0
a=''
for i in range(n):
    a+=str(t)+' '
    t+=r
print(a[:-1])

n,r=map(int,input().split())
print(*[r*i for i in range(n)])


x=' '.join(myTuple)
