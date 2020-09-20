n = int(input())
c=1
d=[]
for i in range(n):
    for j in range(i+1):
        d.append(str(c))
        c+=1
    print(' '.join(d))
    d=[]



