#adding all the edges given an matrix of NxN
n=int(input())
t=0
for i in range(n):
    l=input()
    b=[int(x) for x in l.split(' ')]
    if i==0 or i==n-1:
        t+=sum(b)
    else:
        t+=b[0]+b[n-1]
print(t)
