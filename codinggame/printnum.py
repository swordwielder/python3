d,s=[int(i) for i in input().split()]
a=[9]*d
d=9*d
i=len(a)-1
while d>s:
 if a[i]==1:i-=1
 a[i]-=1
 d-=1
print(*a,sep="")
