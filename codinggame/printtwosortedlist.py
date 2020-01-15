a=[]
b=[]
for i in input().split():
    a.append(int(i))
for i in input().split():
    b.append(int(i))
a.sort()
b.sort()
d=""
for i in range(len(a)):
    d+='('+str(a[i])+', '+str(b[i])+'), '
print(d[:-2])
