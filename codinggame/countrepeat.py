n=str(input())
c=1
m=1
for i in range(1,len(n)):
    if n[i]==n[i-1]:
        m+=1
        if c<m:
            c=m
    else:
        m=1
print(c)
