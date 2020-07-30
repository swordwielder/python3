m=int(input())
for i in range(m):
    n=int(input())
    d=2
    f=[]
    while n>1:
        if n%d==0:
            f.append(d)
            n=n/d
        else:
            d+=1
    print(f[-1])
