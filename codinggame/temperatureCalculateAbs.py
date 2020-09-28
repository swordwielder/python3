
n = int(input()) 
a=[int(i) for i in input().split()]
if len(a)<1:
    print(0)
else:
    d=abs(a[0])
    for i in a:
        if abs(d)>abs(i):
            d=i
            if i<0:
                d=i
        if abs(i)==abs(d) and i>0:
                d=i
    print(d)
