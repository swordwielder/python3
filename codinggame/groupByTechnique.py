from itertools import groupby
n = input()
print(''.join( str(len(list(g))) + k for k, g in groupby(n)))



n = input()
a=n[0]
c=1
r=''
for i in range(1,len(n)):
    if n[i]==a:
        c+=1
    else:
        r+=str(c)+str(n[i-1])
        c=1
        a=n[i]
print(r+str(c)+n[len(n)-1])

