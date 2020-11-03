#my sol
n = int(input())
c=0
a=''
for i in range(n):
    line=input()
    if a=='':
        a=line[0]
    for j in line:
        if j==a:
            c+=1
        else:
            if c==1:
                print(a,end='')
            else:
                print(str(c)+a,end='')
            a=j
            c=1
if c==1:
    print(j,end='')
else:
    print(str(c)+j,end='')




#sol2 
n = int(input())
r=""
l=""
for i in range(n):
    l += input()
t=l[0]
k=1
for i in range(1,len(l)):
    if l[i]==t:
        k+=1
    else:
        if k==1:
            r+=t
        else:
            r+=str(k)+t
        k=1
    t=l[i]
if k==1:
    r+=t
else:
    r+=str(k)+t
        

print(r)
